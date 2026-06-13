## Session 13 — 2026-06-12

### What We Covered
- List indexing review — `items[0]`, `items[-1]`, `len(items)` (opening drill, 2+ sessions ago)
- `list[i] = value` — modifying an item in place by index
- `"[x] " + items[i]` — prepending a string to mark an item done
- `int(input()) - 1` — converting 1-based user input to 0-based index
- Input validation — checking `choice < 1 or choice > len(items)` before updating
- `return` to exit early from a function on invalid input

### Puzzles Completed
- `puzzles/mark_done.py`

### Vocabulary Introduced
- (none new)

### What He Struggled With
- Condition logic: used `and` instead of `or` for invalid range check
- Update ran before the validation check — order was backwards initially

### What Felt Solid
- Caught `input()` inside function was wrong (parameter should come from caller)
- Caught `print(print_list(...))` printing `None` himself
- Fixed `<= 1` to `< 1` after testing edge case himself
- Order issue (check before update) — caught it when prompted, not fully unprompted yet

### Where to Start Next Session
- Placement weak spot: still active — surfaced again (check after update), caught when prompted
- Next: Step 14 — storing a return value in a variable (`result = function()`), needed for BUILD v0.2
- After Step 14: BUILD v0.2 — mark items done in the shopping list app
