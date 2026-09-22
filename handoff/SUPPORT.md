# Support and Update Boundary

Record here after rendering:

- Distribution provider: {{DISTRIBUTION_PROVIDER}}
- Update channel: {{UPDATE_CHANNEL}}
- Support contact/link: {{SUPPORT_URL}}
- Current release: 0.1.2

Framework updates are independent of tenant knowledge.

An update must not overwrite:

- tenant `instance.yaml`;
- Super Second Brain `registry.json`;
- Super Second Brain `state.json`;
- Child-Brain knowledge;
- tenant-private configuration.

If no update relationship is desired, set the instance update mode to `detached`.
