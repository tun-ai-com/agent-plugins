# Changelog

All notable changes. Versions follow SemVer; the plugin version is in `tunai-jobs/.claude-plugin/plugin.json`.

## Unreleased

## 0.1.0 (2026-10-18)

First release.

- `tunai-jobs` plugin for Claude Code: the `tunai` MCP server (https://mcp.tun-ai.com/mcp) and three skills, `find-jobs`,
  `cv-tune-up` and `salary-check`.
- Codex files: `codex/config.toml.example` and `codex/AGENTS.md.snippet`.
- The tools: `search_jobs`, `get_job`, `list_markets`, `salary_for_role`, `get_employer`, `who_is_hiring`, `check_cv_ats`,
  `match_cv_to_job`, `find_jobs_for_cv`. Read only; a CV is read for one call and not stored.
- Repository set up: Gitflow branches, contributing guide, security policy, CI checks.
