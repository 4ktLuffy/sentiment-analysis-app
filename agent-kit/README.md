# Agent Kit

Four tools that work together: two coding agents, one token router that feeds
them, and a skills catalog that tells them how to work.

Everything below was verified by reading each project's own source on
2026-08-27 — the install commands, entry points, and version constraints come
from their `pyproject.toml` / `Makefile` / README, not from memory.

---

## The four

| Tool | What it is | Runs as |
|---|---|---|
| [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | Terminal coding agent, 40+ tools, skills + plugins + MCP | `hermes` |
| [esengine/DeepSeek-Reasonix](https://github.com/esengine/DeepSeek-Reasonix) | DeepSeek-native terminal agent, Go, built for long sessions | `reasonix` |
| [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | Model router — one catalog, 9 agent front-ends | `fcc-*` |
| [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) | Index of 1000+ skills hosted in their own repos | files on disk |

How they compose: **fcc supplies the model → hermes or reasonix does the work →
skills tell it how.** fcc has an `fcc-hermes` launcher specifically, so hermes
can run on fcc's model catalog rather than its own provider config.

---

## Install

Run these on your own machine. Each is the command the project documents.

**hermes-agent**
```bash
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash
```
```powershell
iex (irm https://hermes-agent.nousresearch.com/install.ps1)
```
Needs Python **3.11–3.13**. The upper bound is enforced upstream and is not
cosmetic: on 3.14 there is no `cp314` wheel for `pydantic-core`, so it falls
back to a maturin source build that fails. The installer drops a full git
checkout at `~/.hermes/hermes-agent`.

**DeepSeek-Reasonix**
```bash
npm i -g reasonix                          # any OS, pulls the prebuilt binary
brew install esengine/reasonix/reasonix    # macOS
```
Also ships a VS Code extension (`SivanLiu.reasonix-agent` on the Marketplace,
or Open VSX for VSCodium/Theia). Building from source needs Go 1.25+:
`CGO_ENABLED=0 go build -o bin/reasonix ./cmd/reasonix`.

**free-claude-code**
```bash
curl -fsSL "https://raw.githubusercontent.com/Alishahryar1/free-claude-code/main/scripts/install.sh" | sh
```
```powershell
& ([scriptblock]::Create((irm "https://raw.githubusercontent.com/Alishahryar1/free-claude-code/main/scripts/install.ps1")))
```
Launchers it installs: `fcc-claude`, `fcc-codex`, `fcc-pi`, `fcc-opencode`,
`fcc-cline`, `fcc-hermes`, `fcc-dsh`, `fcc-grok`, `fcc-muse`, `fcc-aider`,
plus `fcc-server` and the `fcc-desktop` GUI. Voice support is opt-in via
`--voice-local`, `--voice-nim`, or `--voice-all`.

Uninstall is symmetric (`scripts/uninstall.sh`), and removes `~/.fcc/` while
leaving the agents themselves installed.

---

## Credentials

None of the three CLIs do anything until you connect a model. **This is on you
— no script here logs you into anything.**

- **fcc** routes across ~50 providers; you connect the accounts you want through
  its UI. It states it follows provider terms and drops integrations that stop
  being permitted — worth reading its notes before you lean on it for volume.
- **hermes** picks a provider with `hermes model`, or rides fcc's catalog via
  `fcc-hermes`.
- **reasonix** is DeepSeek-native and wants a DeepSeek key, or an fcc-routed
  model via `fcc-dsh`.

---

## Skills

`awesome-agent-skills` is an **index only** — every skill lives in its own repo.
So "installing" it means copying skill folders into an agent's skills directory.

Paths, per the index:

| Tool | Project | Global |
|---|---|---|
| Claude Code | `.claude/skills/` | `~/.claude/skills/` |
| Gemini CLI | `.gemini/skills/` | `~/.gemini/skills/` |
| hermes | `skills/` in its checkout | `~/.hermes/…` |

A good starting set for working an unfamiliar codebase — all from
[mattpocock/skills](https://github.com/mattpocock/skills) (MIT), under
`skills/engineering/`:

- `wayfinder` — plan work too big for one session as decision tickets
- `triage` — move issues and external PRs through a triage state machine
- `diagnosing-bugs`
- `code-review`
- `improve-codebase-architecture`
- `resolving-merge-conflicts`
- `research`
- `tdd`

Pull them with a sparse checkout:

```bash
git clone --depth 1 --filter=blob:none --sparse https://github.com/mattpocock/skills /tmp/mp
git -C /tmp/mp sparse-checkout set skills/engineering
mkdir -p .claude/skills
cp -r /tmp/mp/skills/engineering/{wayfinder,triage,diagnosing-bugs,code-review} .claude/skills/
```

Other catalogs the index points at: [NVIDIA/skills](https://github.com/NVIDIA/skills)
(344 skills, mostly NVIDIA-product-specific) and `officialskills.sh` for
first-party skills from OpenAI, Cloudflare, Sentry, Trail of Bits, and others.

---

## One caution

`awesome-agent-skills` and the skill repos it links are community-contributed
code that your agent will execute with your permissions. The index carries its
own security notice for a reason. Read a `SKILL.md` before you install it —
especially any that shell out.
