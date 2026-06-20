## Session 21 — 2026-06-19

### What We Covered
- Opening REPL drill: f-strings with `:.2f` (session 17 concept)
- `key not in dict` — checking before adding a new key to avoid KeyError
- BUILD v0.1 of expense tracker — full working core, no file saving

### Puzzles Completed
- `projects/expense_tracker.py` (BUILD v0.1)

### Vocabulary Introduced
- (none new)

### What He Struggled With
- Placed `expenses = []` inside the `while True` loop — needed a prompt to catch it (placement streak reset to 0)
- `!= in` — tried to combine operators instead of using `not in`
- `total.append()` — used list method on a dict; needed redirect to DRILLS.md

### What Felt Solid
- Caught that `category_totals.py` was hardcoded — good observation
- Understood `not in` quickly once the drill was done
- Explained final concept back correctly: initializing the key to 0 so the add line always has something to work with
- `float` fix identified immediately when asked

### Where to Start Next Session
- Placement weak spot: streak at 0 — placed `expenses = []` inside loop, needed a hint
- Next: Step 6 — saving and loading a list of dicts to/from a file
- File I/O was covered in session 15 (`goal_saver.py`) but this is more complex — dicts with three fields
- Do extra REPL drilling before the puzzle (roadmap has two drill checkboxes for this step)
