# Security

## Reporting a vulnerability

Please do not open a public issue for a security problem.

Report it privately, either way:

- Use GitHub's private reporting: the **Security** tab of this repo, then **Report a vulnerability**.
- Or email **praveenkpandu2@gmail.com** with "TUNAI agent plugins security" in the subject.

Say what you found, how to reproduce it, and what it could do. We will answer within three working days and tell you when it is fixed.

## What is in scope

- The plugin files in this repo: skills, MCP configuration, the checks under `scripts/`.
- A skill that could lead an assistant to leak a key or a CV, or to act beyond the read only tools.
- The hosted server at `mcp.tun-ai.com` and the key dashboard at `tun-ai.com/agents`. Report those the same way.

## Keys

Your key is yours. Keep it in the `TUNAI_API_KEY` environment variable and never paste it into an issue, a pull request or a
chat. You can revoke any key at https://tun-ai.com/agents/dashboard. If a key leaks, revoke it there first.

CI scans every pull request for strings that look like a TUNAI key and fails if it finds one.
