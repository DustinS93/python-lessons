## Session 14 — 2026-06-13

### What We Covered
- Opening REPL drill: `.pop()` removes and returns the last item — value can be caught in a variable
- `result = function()` — storing a return value before using it
- REPL drills: `double(result)`, `message = add_greeting()`, direct vs stored return value
- Validation placement — check belongs in main code, not inside a helper function
- Puzzle: two clean functions, store-then-validate-then-act pattern

### Puzzles Completed
- `puzzles/name_badge.py`

### Vocabulary Introduced
- (none new)

### What He Struggled With
- Placement (x3 in one puzzle): validation inside `get_name()`, then `make_badge()` called before empty check, then `badge` stored outside the `else` block — each caught when prompted, none unprompted

### What Felt Solid
- REPL drills clicked fast — chained return values, understood argument vs parameter unprompted
- Recognized the tangling problem himself once asked about it
- Final structure was clean: get → store → check → act

### Where to Start Next Session
- Placement weak spot: still very active — 3 placement mistakes in one puzzle, all caught when prompted
- Step 14 complete — both checkboxes done
- Next: BUILD v0.2 — mark items done in shopping list app
