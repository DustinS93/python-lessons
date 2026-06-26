## Session 24 — 2026-06-25

### What We Covered
- Warm-up placement drill: `return` inside a for loop — predicted output of a summing function (caught the trap after one nudge)
- REPL drill: `.pop(index)` — returns the *item* removed, not the index; deletes in place
- Stretch feature: Delete an expense by number — new `elif`, `print_list()` reuse, `pop(n - 1)` bridge
- Off-by-one bridge: user types `1` (1-based display) → `expenses.pop(n - 1)` (0-based list)
- Diagnosed the real bug himself: deletes "not saving" because hard-close skipped `break`, so the after-loop `save_expenses` never ran
- Fix: saving-on-write — call `save_expenses(expenses)` inside Add and Delete blocks

### Puzzles Completed
- `projects/expense_tracker.py` (BUILD — Delete feature + save-on-write)

### Vocabulary Introduced
- DRY (Don't Repeat Yourself), saving-on-write

### What He Struggled With
- Guessed at the bug 3× ("not saving", "global doesn't work", "save the return") before running the app — theorized instead of observing
- "Reaching for a global to read it doesn't work" — wrong; reading a global inside a function is fine, only reassigning is the trap
- Confused pop's return (the item) with the index argument
- Explain-back: knew the fix but struggled to articulate the placement/timing *concept* (needed scaffolding)

### What Felt Solid
- Placement CLEAN and unprompted: new `elif`, both `save_expenses` calls, `pop` not trapped in a loop
- Reached for DRY unprompted — built `print_list()`, then cleaned View All to call it
- Self-diagnosed the hard-close-skips-save bug and proposed save-on-write himself

### Where to Start Next Session
- Placement: 1 clean build appearance this session (streak 0 → 1) — needs 1 more clean unprompted appearance to re-eliminate
- Reinforce debugging discipline: RUN it before theorizing (recurring pattern this session)
- Next: more stretch (filter by category / sort by amount), or start the next roadmap (Pygame/Tkinter)
