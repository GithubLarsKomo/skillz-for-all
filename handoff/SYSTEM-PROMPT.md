# System Prompt Hook Template

The tenant prompt points to recipient-owned Google Drive objects rather than a source-owner repository.

Recommended minimal hook:

```text
For substantive work, use the Google Drive Second-Brain bootstrap identified by {{SUPER_SECOND_BRAIN_BOOTSTRAP_FILE_ID}} as the constant Second-Brain bootstrap.
```

Recommended companion rule:

```text
Use the tenant Skillz framework rooted at Google Drive folder {{FRAMEWORK_ROOT_FOLDER_ID}} for normative workflow contracts. Before completion or handoff of substantive work, apply its Knowledge Promotion Gate and apply Second-Brain Lint when triggered.
```

Do not embed the entire framework into the system prompt.

The deployment is valid only after the placeholders above have been rebound to recipient-owned Drive IDs and read-back verified.
