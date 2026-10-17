# TUNAI for AI assistants

Ask your assistant for live jobs, a CV tune-up, or what a role pays, and get answers from employers' own career pages.
Works with Claude Code, Codex, Cursor and any MCP client. Read only. Free key.

> "Find me ten data analyst jobs in Leeds, then tell me what to add to my CV."
> "What does a staff nurse advertise as pay in Birmingham, and who is hiring?"
> "Check this CV the way a recruiting system reads it."

## What you get

| Tool | What it does |
|---|---|
| `search_jobs`, `get_job` | Live jobs with pay when the advert states it, and a link to apply on the employer's page |
| `find_jobs_for_cv` | Reads a CV and returns jobs that fit it, with the skills the CV already shows and the ones to add |
| `match_cv_to_job` | One CV against one job: which required skills it names, which it does not |
| `check_cv_ats` | How a recruiting system reads the CV, with the fixes |
| `salary_for_role` | Pay by level, with its sample size and the date it was measured |
| `who_is_hiring`, `get_employer` | The employers with the most open roles for a title, and one employer's page in data |
| `list_markets` | The countries covered |

Honest by design: every number comes with its sample and date, a thin result is withheld and says so, and a job that is not
the person's kind of work is left out rather than padded in.

## Install

Get a free key at https://tun-ai.com/agents (sign in with your email, no card).

### Claude Code

```
export TUNAI_API_KEY=your_key
/plugin marketplace add tun-ai-com/agent-plugins
/plugin install tunai-jobs@tunai
```

You get the `tunai` MCP server and three skills: `find-jobs`, `cv-tune-up` and `salary-check`. Without the plugin:

```
claude mcp add --transport http tunai https://mcp.tun-ai.com/mcp --header "Authorization: Bearer $TUNAI_API_KEY"
```

### Codex

Copy `codex/config.toml.example` into `~/.codex/config.toml` and `codex/AGENTS.md.snippet` into your `AGENTS.md`.

### Any other MCP client

Server `https://mcp.tun-ai.com/mcp`, streamable HTTP, header `Authorization: Bearer <key>`.
Docs for agents: https://tun-ai.com/agents/docs.md

## Your data

- A CV you send is read to answer that one call. It is not stored.
- The tools are read only: nothing is applied for, sent or changed on your behalf.
- Job adverts are written by third parties. The skills tell your assistant to report them and never follow instructions
  inside them.
- Keys are yours: see use and revoke any key at https://tun-ai.com/agents/dashboard.

## Limits

Free keys have a daily allowance for calls and for CV tools. A TUNAI paid account raises the limits. Current numbers are on
https://tun-ai.com/agents.

## Contributing

Branches follow Gitflow: `main` is what people install, `develop` is the next release. See [CONTRIBUTING.md](CONTRIBUTING.md).
Security problems: [SECURITY.md](SECURITY.md). Changes: [CHANGELOG.md](CHANGELOG.md).

## About

Built by TUNAI (https://tun-ai.com). MIT licence. Not affiliated with Anthropic or OpenAI.
