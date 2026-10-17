## What and why

<!-- One or two sentences. Link the issue if there is one. -->

## Target branch

- [ ] `develop` (a feature or fix). Releases and hotfixes are opened by maintainers.

## Checklist

- [ ] `python scripts/check.py` passes
- [ ] I tried the change on a real client (Claude Code, Codex or another), or it only touches docs
- [ ] Nothing here tells an assistant to apply, send or change anything for the user (the tools are read only)
- [ ] No figure is stated that the tools do not return; no real CV, key or personal data is included
- [ ] No em dashes in text an assistant or a person reads
- [ ] If this is a release: the version in `plugin.json` and `marketplace.json` match and `CHANGELOG.md` has the entry
