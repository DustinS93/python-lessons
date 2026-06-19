## Session 19 — 2026-06-18

### What We Covered
- Opening REPL drill: list of dicts — looping, accessing fields (session 16 concept)
- f-strings — `f"{variable}"`, `f"{value:.2f}"` for fixed-point decimals
- `:.2f` format spec — always show 2 decimal places, dependent on f-string prefix
- `.capitalize()` — string method, first letter uppercase
- Passing dict values as separate arguments to a function
- Key insight: dict keys and function parameter names are separate things that can share the same spelling

### Puzzles Completed
- `puzzles/receipt_printer.py`
- `puzzles/menu_board.py`

### Vocabulary Introduced
- `.capitalize()`

### What He Struggled With
- `receipt_printer.py`: used `e["desc"]` inside function instead of parameters — function was ignoring its own arguments, reading global `e`
- Confusion between dict keys, parameter names, and loop access when all have similar names ("inception" effect)
- Needed redirect to separate the loop from the function (loop inside function vs loop calling function)

### What Felt Solid
- `:.2f` clicked after one explanation and drills
- Correctly identified that `.capitalize()` can't be called on a float
- `menu_board.py`: header placed outside the loop unprompted — first clean placement appearance this session
- Articulated parameter passing correctly in plain English at end of session

### Where to Start Next Session
- Placement weak spot: first clean unprompted appearance (menu_board.py header). One more needed to eliminate.
- Next: Step 4 — summing values from a list of dicts (REPL drill first)
- Design next puzzle to surface placement weak spot again
