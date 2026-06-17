## Session 17 — 2026-06-15

### What We Covered
- Opening REPL drill: dictionary basics — accessing, updating, adding keys, `.keys()`, `len()`
- `try/except ValueError` — catching errors from bad user input instead of crashing
- `not in range(len(list))` — checking for out-of-range input
- Why logic inside `try` block matters — anything after a failed line is skipped, variables never assigned

### Puzzles Completed
- `puzzles/number_picker.py`

### Vocabulary Introduced
- (none new)

### What He Struggled With
- `if choice != 0 or 1 or 2` — thought this checked all three values; learned `or 1` is always truthy
- Placement: `choice = choice - 1` and conditionals initially outside `try` block — caught it himself mid-puzzle after NameError
- `try/except` explanation at session end slightly incomplete — named the what but not the why on placement

### What Felt Solid
- Diagnosed NameError himself: "choice only gets assigned if the try block succeeds" — correct, unprompted
- Used `range(len(grocery_list))` independently — cleaner than a hardcoded list
- Simplified `if/elif` chain to `grocery_list[choice]` unprompted

### Where to Start Next Session
- Placement weak spot: surfaced again — but Dustin caught it himself this time (NameError → diagnosis → fix). Progress.
- Next: apply try/except to shopping_list.py, or a second try/except puzzle before moving on
- `try/except` is new — worth one more rep before moving on
