## Session 12 — 2026-06-11

### What We Covered
- `return` inside a loop — opening drill, 2nd consecutive clean appearance (eliminated)
- `None` — Python's "nothing" value, always capital N. REPL suppresses it; `print()` shows it
- Case sensitivity — `None` vs `none`, Python distinguishes uppercase from lowercase everywhere
- `while True / break` — loops forever until `break` fires; use when no value exists to check at loop start
- `break` vs `return` — `break` exits the loop, `return` exits the entire function
- BUILD v0.1 — first working version of the shopping list app

### Puzzles Completed
- `puzzles/menu_loop.py`
- `projects/shopping_list.py` (BUILD v0.1)

### Vocabulary Introduced
- `None`
- case-sensitive
- `break`

### What He Struggled With
- Used `return` instead of `break` in menu puzzle — needed reminder of the distinction
- REPL showing nothing for `None` return — confused about whether function ran

### What Felt Solid
- `while True` rationale — explained correctly that no condition exists yet at loop start
- `shopping_list = []` outside the loop — caught the reset problem when asked
- BUILD v0.1 structure clean — loop, list, append, numbered view, break on quit all correct

### Where to Start Next Session
- `return` inside loop: ELIMINATED — 2 consecutive clean appearances (sessions 11 and 12)
- Placement weak spot: still active — surfaced in menu puzzle (return vs break)
- Next: Step 13 — modifying list items `list[i] = value`, needed for marking items done (BUILD v0.2)
