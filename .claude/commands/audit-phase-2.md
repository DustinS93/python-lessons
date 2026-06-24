# Audit Phase 2 — Instruction Audit

Check CLAUDE.md for contradictions, ambiguities, and rules that don't map cleanly to the actual file structure or workflow.

## Steps

1. Read `CLAUDE.md` in full.
2. Read `DRILLS.md`, `PROGRESS.md`, `PROGRESS_LOG.md`, and `ROADMAP.md`.
3. For each rule or instruction in CLAUDE.md, ask:
   - Is it unambiguous? Could it be interpreted two different ways?
   - Does it reference a file or folder that actually exists?
   - Does it conflict with any other rule in CLAUDE.md?
   - Is it realistic given the actual project structure?
4. Check the Session Start and Session End rules — do they match what PROGRESS.md and DRILLS.md actually track?
5. Check the Recurring Weak Spots rules — is the elimination criteria (2 consecutive puzzle appearances, unprompted, no struggle) clearly trackable with the current system?
6. Check the Git Habits rules — are they consistent with the current project state?

## Report Format

- **Contradictions**: list any rules that conflict with each other
- **Ambiguities**: list any rules that are unclear or could be read two ways
- **Dead references**: any file/folder mentioned that doesn't exist
- **Structural mismatches**: rules that don't fit the actual workflow
- **Summary**: one sentence verdict and top recommendation if any
