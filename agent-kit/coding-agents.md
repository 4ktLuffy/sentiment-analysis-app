# Coding Agents & Harnesses

Five tools, studied from source on 2026-08-27. Commands, counts, and caveats
below come from each project's own files — not from their marketing copy.

The important thing first: **these are not five alternatives to choose between.**
They sit at three different layers, and the useful setups combine them.

```
Layer 0   free-claude-code        supplies the model
             │
Layer 1   hermes · Reasonix · MetaGPT     standalone agents that do work
             │
Layer 2   ECC                     upgrades the agent you already use
```

---

## Pick by what you're doing

| You want to… | Reach for | Why |
|---|---|---|
| Make your existing Claude Code sharper today | **ECC** | Installs into Claude Code itself. No new tool to learn. |
| Talk through an unfamiliar codebase | **hermes** | Conversational, 40+ tools, 37 skills built in. |
| Run one defined task, no conversation | **Reasonix** | `reasonix run "…"` is scriptable and non-interactive. |
| Batch the same job over many repos | **Reasonix** | Same reason — it's the only one with a clean one-shot form. |
| Generate a whole project from one prompt | **MetaGPT** | Role-based multi-agent; writes specs then code. |
| Stop paying per token while experimenting | **free-claude-code** | Routes free provider tokens into the agents above. |

---

## ECC (affaan-m/ECC)

**What it is:** not an agent — a harness upgrade. It installs 94 slash commands
and 68 agents into Claude Code, plus hooks that enforce plan → test → review
gates *outside* the model's context, so they don't get forgotten mid-session.

**Install** — run inside Claude Code:
```text
/plugin marketplace add https://github.com/affaan-m/ECC
/plugin install ecc@ecc
```

> **Do not stack install methods.** The README is explicit: installing ECC twice
> into the same harness duplicates skills, commands, and hooks. Plugin install
> *or* manual install, never both. Installing once into several different
> harnesses (Claude Code + Codex) is fine.

> **Official sources only.** The project warns that third-party mirrors may
> carry malware. Trust only: the GitHub repo, npm `ecc-universal` /
> `ecc-agentshield`, the `ecc-tools` GitHub App, plugin slug `ecc@ecc`, and
> ecc.tools.

**How to call it** — type `/` in any Claude Code session. The commands that
matter most:

| Command | Use when |
|---|---|
| `/plan` | Starting a feature. Writes a step-by-step plan and **waits for your confirm before touching code.** |
| `/code-review` | Code just written. Local changes, or pass a PR number for PR mode. |
| `/build-fix` | Build broken. Auto-delegates to the right language resolver. |
| `/python-review` | Python-specific pass: PEP 8, type hints, security. |
| `/test-coverage` | Find coverage gaps and generate the missing tests. |
| `/santa-loop` | High-stakes code. Two independent model reviewers must *both* approve before it ships. |
| `/save-session` · `/resume-session` | Ending work for the day / picking it back up. |
| `/learn-eval` | End of a session that went well — extracts reusable patterns and self-scores them. |
| `/evolve` · `/instinct-status` | Review what it has learned, with confidence scores. |
| `/skill-create` | Turn your git history into a reusable skill. |
| `/loop-start` | Repeated task on an interval. |

**When it's useful:** immediately and daily, if Claude Code is already your main
tool. It's the lowest-friction of the five — no new CLI, no separate model
config.

**When it isn't:** if you want an agent that runs *outside* Claude Code, or you
dislike opinionated workflow enforcement. 94 commands is a lot of surface;
start with `/plan`, `/code-review`, `/build-fix` and ignore the rest until
you need them.

---

## hermes-agent (NousResearch)

**What it is:** a full terminal coding agent — 40+ tools, 15 built-in skills
plus 22 optional ones, plugins, MCP support, and a messaging gateway.

**Install:**
```bash
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash
```
Needs Python **3.11–3.13**. The ceiling is enforced upstream and is not
cosmetic: on 3.14 there's no `cp314` wheel for `pydantic-core`, so it falls back
to a source build that fails. Lands a git checkout at `~/.hermes/hermes-agent`.

**How to call it:**
```bash
hermes setup      # one-shot wizard: provider, model, tools
hermes            # interactive session
hermes model      # switch provider/model
hermes tools      # toggle which of the 40+ tools are live
hermes doctor     # diagnose a broken install
hermes gateway    # drive it from Telegram/Discord
```

**When it's useful:** open-ended work where you don't yet know the shape of the
problem. Exploring a codebase, debugging something weird, long sessions where
the conversation itself is doing useful work. The gateway is genuinely
different — it's the only one of the five you can drive from your phone.

**When it isn't:** scripted or batch work. Its documented modes are interactive
and gateway; there's no clean one-shot flag in the README.

---

## Reasonix (esengine/DeepSeek-Reasonix)

**What it is:** a DeepSeek-native terminal agent written in Go, engineered
around prefix-cache stability — the design goal is that you leave it running.

**Install:**
```bash
npm i -g reasonix                          # any OS, prebuilt binary
brew install esengine/reasonix/reasonix    # macOS
```
Also a VS Code extension (`SivanLiu.reasonix-agent`, or Open VSX for
VSCodium/Theia) and a desktop app. From source needs Go 1.25+.

**How to call it:**
```bash
reasonix setup                                   # provider + model
reasonix                                         # interactive
reasonix run "implement the TODOs in main.go"    # one-shot, non-interactive
```
Inside a session, `/init` generates project instructions for the current repo.

**When it's useful:** you know exactly what you want done. The `run` form is the
one genuinely distinct capability across all five — it's scriptable, so you can
loop it across a list of repos or wire it into CI.

**When it isn't:** exploratory work. Also defaults to DeepSeek, so it's a second
API key unless you route it through fcc with `fcc-dsh`.

---

## MetaGPT (FoundationAgents)

**What it is:** a multi-agent framework that assigns software-company roles —
product manager, architect, engineer — and runs them in sequence to turn one
prompt into specs, diagrams, and code.

**Install:**
```bash
conda create -n metagpt python=3.9 && conda activate metagpt
pip install --upgrade metagpt
metagpt --init-config    # writes ~/.metagpt/config2.yaml — edit it
```

**How to call it:**
```bash
metagpt "Create a 2048 game"    # writes a new repo into ./workspace
```

**When it's useful:** greenfield generation. You want a working skeleton plus
the design artifacts (requirements, architecture) that normally get skipped.
Good for prototyping an idea end to end.

**When it isn't:** working inside an existing codebase. It generates *into
`./workspace`* — it's a project generator, not a repo editor. Don't reach for it
to fix a bug in code you already have.

---

## free-claude-code (Alishahryar1)

**What it is:** a model router. Connect provider accounts once, then drive any
of 10 agent front-ends off that one catalog.

**Install:**
```bash
curl -fsSL "https://raw.githubusercontent.com/Alishahryar1/free-claude-code/main/scripts/install.sh" | sh
```

**How to call it:**
```bash
fcc-server        # Linux — keep this terminal open. macOS/Windows: launch the app.
```
Then in the Admin UI it opens: create a key at
`build.nvidia.com/settings/api-keys`, paste into `NVIDIA_NIM_API_KEY`, leave
`MODEL` on the default `nvidia_nim/nvidia/nemotron-3-super-120b-a12b`,
**Validate** → **Apply**.

Launchers: `fcc-claude`, `fcc-codex`, `fcc-pi`, `fcc-opencode`, `fcc-cline`,
`fcc-hermes`, `fcc-dsh`, `fcc-grok`, `fcc-muse`, `fcc-aider`, plus `fcc-server`
and the `fcc-desktop` GUI.

**When it's useful:** experimenting. It makes running hermes and Reasonix
effectively free, which matters when you're learning them and burning tokens on
throwaway sessions.

**When it isn't:** anything you depend on. It's a routing layer over third-party
free tiers — availability moves. Note it says it drops integrations that stop
being permitted, so read its provider notes before leaning on it for volume.

---

## Suggested order

1. **ECC** — biggest immediate gain, installs into what you already use.
2. **fcc** — set up the NVIDIA NIM key so the next two cost nothing.
3. **hermes** via `fcc-hermes` — learn it on free tokens.
4. **Reasonix** when you hit a task you want scripted rather than discussed.
5. **MetaGPT** only when you're starting something from scratch.

Two of these need nothing but a terminal and five minutes; the other three need
a model connected before they do anything at all.
