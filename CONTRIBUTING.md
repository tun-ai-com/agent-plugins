# Contributing

Thanks for helping. This repo holds the TUNAI plugins for AI assistants. It is small on purpose: skills, MCP
configuration and a few docs. The server lives at https://mcp.tun-ai.com and is not in this repo.

## Branches (Gitflow)

| Branch | What it is | Who writes to it |
|---|---|---|
| `main` | What people install. Every commit on it is a release, tagged `vX.Y.Z`. | Release and hotfix pull requests only |
| `develop` | The next release, integrated. Open your pull request against this. | Pull requests only |
| `feature/<topic>` | One change: a skill, a doc, a config fix. | You. Branch from `develop`, return to `develop`, squash merged |
| `release/X.Y.Z` | The freeze before a release: version bump, changelog, install test. | Maintainers. Branch from `develop`, merge to `main` and back to `develop`, then tag |
| `hotfix/X.Y.Z` | A broken install or a wrong claim on `main`. | Maintainers. Branch from `main`, merge to `main` and `develop`, then tag |

`main` is the default branch because Claude Code's `/plugin marketplace add` reads it. That is why nothing reaches it
without a release.

### Making a change

1. Fork the repo, then branch from `develop`: `git switch -c feature/short-name develop`.
2. Make the change. Run `python scripts/check.py`. It is the same check CI runs.
3. Open a pull request into `develop`. Fill in the template.
4. A maintainer reviews and squash merges.

### Releasing (maintainers)

1. `git switch -c release/X.Y.Z develop`.
2. Bump the version in `tunai-jobs/.claude-plugin/plugin.json` and `.claude-plugin/marketplace.json` (they must match; CI checks)
   and add the entry to `CHANGELOG.md`.
3. Install the plugin from the release branch on a real client and run each skill once.
4. Pull request `release/X.Y.Z` into `main`. After the merge, tag `vX.Y.Z` on `main` and open a pull request from `main` back
   into `develop` so the version bump is not lost.

### Hotfix

Branch `hotfix/X.Y.Z` from `main`, fix, pull request into `main`, tag, then merge `main` into `develop`.

## What a skill may and may not do

- The tools are read only. A skill must never tell an assistant to apply, send or change anything for the user.
- A skill must say where a figure comes from and never invent one. Pay is what adverts state, with a sample and a date.
- Job advert text is written by third parties. A skill treats it as data to report, never as instructions.
- A CV is read to answer one call. A skill must not tell an assistant to send a CV the user did not ask it to check.
- Write plainly. No em dashes in anything an assistant or a person reads.

## Reporting a problem

Bugs and ideas for the next tool: open an issue. Security problems: see [SECURITY.md](SECURITY.md), not an issue.
