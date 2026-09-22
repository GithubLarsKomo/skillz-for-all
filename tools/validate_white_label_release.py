#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

REQUIRED = [
    "00-START-HERE.md",
    "instance.yaml",
    "deployment-manifest.json",
    "release/manifest.json",
    "release/SHA256SUMS.json",
    "framework/docs/KNOWLEDGE-STORE-CONTRACT.md",
    "framework/docs/DRIVE-STORAGE-AND-DELIVERY-CONTRACT.md",
    "framework/skills/artifact-contract-audit/SKILL.md",
    "framework/skills/artifact-production-contract/SKILL.md",
    "framework/docs/DOCUMENT-ARTIFACT-DELIVERY-CONTRACT.md",
    "framework/docs/ARTIFACT-PRODUCTION-CONTRACT.md",
    "framework/docs/KNOWLEDGE-PROMOTION-CONTRACT.md",
    "framework/docs/SECOND-BRAIN-LINT-CONTRACT.md",
    "framework/skills/project-second-brain/SKILL.md",
    "framework/skills/second-brain-federation-workflow/SKILL.md",
    "second-brain/super-second-brain/docs/super-memory/BOOTSTRAP.md",
    "second-brain/super-second-brain/docs/super-memory/registry.json",
]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()




def parse_skill_frontmatter(path: Path) -> tuple[str | None, list[str]]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return None, []
    end = text.find("\n---\n", 4)
    if end < 0:
        return None, []
    lines = text[4:end].splitlines()
    name: str | None = None
    requires: list[str] = []
    current: str | None = None
    for line in lines:
        if line.startswith("name:"):
            name = line.split(":", 1)[1].strip().strip("\"'")
            current = None
            continue
        if line.startswith("requires:"):
            current = "requires"
            inline = line.split(":", 1)[1].strip()
            if inline == "[]":
                current = None
            continue
        if current == "requires":
            stripped = line.strip()
            if stripped.startswith("- "):
                requires.append(stripped[2:].strip().strip("\"'"))
            elif stripped and not line.startswith(" "):
                current = None
    return name, requires


def validate_skill_graph(root: Path, errors: list[str]) -> None:
    skills_root = root / "framework" / "skills"
    if not skills_root.is_dir():
        errors.append("framework/skills directory missing")
        return
    skill_dirs = {
        path.name: path
        for path in skills_root.iterdir()
        if path.is_dir() and (path / "SKILL.md").is_file()
    }
    for slug, skill_dir in sorted(skill_dirs.items()):
        name, requires = parse_skill_frontmatter(skill_dir / "SKILL.md")
        if name != slug:
            errors.append(
                f"skill name/path mismatch: {slug} declares {name!r}"
            )
        for dependency in requires:
            if dependency not in skill_dirs:
                errors.append(
                    f"missing required skill: {slug} -> {dependency}"
                )

def main() -> int:
    parser = argparse.ArgumentParser(description="Validate a white-label deployment release.")
    parser.add_argument("root", type=Path)
    parser.add_argument("--forbid", action="append", default=[])
    args = parser.parse_args()

    root = args.root.resolve()
    errors: list[str] = []

    for rel in REQUIRED:
        if not (root / rel).is_file():
            errors.append(f"missing required file: {rel}")

    manifest_path = root / "release" / "manifest.json"
    sums_path = root / "release" / "SHA256SUMS.json"
    deployment_path = root / "deployment-manifest.json"

    if sums_path.is_file():
        sums = json.loads(sums_path.read_text(encoding="utf-8"))
        for rel, expected in sums.items():
            path = root / rel
            if not path.is_file():
                errors.append(f"hash target missing: {rel}")
                continue
            actual = sha256(path)
            if actual != expected:
                errors.append(f"hash mismatch: {rel}")

    if manifest_path.is_file():
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        if manifest.get("storageProvider") != "google-drive":
            errors.append("release manifest storageProvider must be google-drive")
        if manifest.get("rebindRequired") is not True:
            errors.append("release manifest must require rebind")
        if manifest.get("runtimeStoragePolicy") != "drive-only":
            errors.append("release manifest runtimeStoragePolicy must be drive-only")
        if manifest.get("sourceExclusionPolicyApplied") is not True:
            errors.append("release manifest must record applied source exclusion policy")

    if deployment_path.is_file():
        deployment = json.loads(deployment_path.read_text(encoding="utf-8"))
        storage = deployment.get("storage", {})
        if storage.get("provider") != "google-drive":
            errors.append("deployment storage provider must be google-drive")
        if storage.get("runtimePolicy") != "drive-only":
            errors.append("deployment runtimePolicy must be drive-only")
        if storage.get("generatedNonCodeArtifacts") != "google-drive-required":
            errors.append("deployment must require generated non-code artifacts in Google Drive")
        if storage.get("linkFirstDelivery") is not True:
            errors.append("deployment must require link-first Drive delivery")
        if deployment.get("runtimeDependencyOnSourceOwner") is not False:
            errors.append("deployment retains source-owner runtime dependency")
        privacy = deployment.get("privacy", {})
        if privacy.get("containsSourceOwnerKnowledge") is not False:
            errors.append("deployment privacy flag allows source-owner knowledge")
        if privacy.get("containsOrganizationSpecificContent") is not False:
            errors.append("deployment privacy flag allows organization-specific content")
        if privacy.get("starterRegistryMustBeEmpty") is not True:
            errors.append("starter deployment must require empty registry")

    instance_path = root / "instance.yaml"
    if instance_path.is_file():
        instance_text = instance_path.read_text(encoding="utf-8")
        if "runtimeStoragePolicy: drive-only" not in instance_text:
            errors.append("instance runtimeStoragePolicy must be drive-only")
        if "provider: google-drive" not in instance_text:
            errors.append("instance primary Knowledge Store must be google-drive")
        if "requireDriveWrite: true" not in instance_text or "returnStoredLinks: true" not in instance_text:
            errors.append("instance delivery must require Drive write and stored-link handoff")

    validate_skill_graph(root, errors)

    registry_path = root / "second-brain" / "super-second-brain" / "docs" / "super-memory" / "registry.json"
    if registry_path.is_file():
        registry = json.loads(registry_path.read_text(encoding="utf-8"))
        if registry.get("brains") != []:
            errors.append("starter Super Brain registry is not empty")

    for path in sorted(root.rglob("*")):
        if not path.is_file():
            continue
        if path.suffix.lower() not in {".md", ".json", ".yaml", ".yml", ".txt", ".py"}:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for token in args.forbid:
            if token and token in text:
                errors.append(f"forbidden token {token!r}: {path.relative_to(root)}")

    if errors:
        print("White-label release validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("OK: white-label release validated")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
