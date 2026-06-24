# Audit Phase 3 — Memory & Tracking Accuracy

Check whether the memory files and progress tracking still reflect reality.

## Steps

1. Read the memory file at: `~/.claude/projects/-Users-dustinsheldon-Documents-1--Projects-python-lessons/memory/user_profile.md`
2. Read `PROGRESS_LOG.md` in full.
3. Read `DRILLS.md` Active Concepts and any weak spot notes.
4. Cross-check weak spots in `user_profile.md` against recent PROGRESS_LOG.md entries:
   - Are listed weak spots still appearing in recent sessions, or have they been resolved?
   - Are there patterns in PROGRESS_LOG.md that should be weak spots but aren't listed?
5. Read all other memory files listed in MEMORY.md and check each one:
   - Is it still accurate given the current project state?
   - Is it stale (refers to something that no longer applies)?
6. Check PROGRESS.md — does it match the most recent PROGRESS_LOG.md entry, or is it out of sync?
7. Check ROADMAP.md checkboxes — do they align with what PROGRESS_LOG.md says has been completed?

## Report Format

- **Weak spots: still active?** list each with status (still appearing / likely resolved / unclear)
- **Weak spots: untracked patterns?** any struggles in PROGRESS_LOG not in user_profile
- **Memory file accuracy**: list any stale or inaccurate entries
- **PROGRESS.md sync**: OK or describe the mismatch
- **ROADMAP.md sync**: OK or describe checkbox drift
- **Summary**: one sentence verdict and recommended memory updates
