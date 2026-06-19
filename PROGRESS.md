## Session 20 — 2026-06-18

### What We Covered
- Opening REPL drill: list of dicts field access (session 16/17 concept)
- Accumulator pattern — `total = 0`, loop, `total = total + item["field"]`
- Grouping and accumulating — dict of totals, `totals[e["category"]] = totals[e["category"]] + e["amount"]`
- Looping over `dict.keys()` to print formatted output with `:.2f` and `.capitalize()`

### Puzzles Completed
- `puzzles/score_total.py`
- `puzzles/category_totals.py`

### Vocabulary Introduced
- accumulator pattern

### What He Struggled With
- `category_totals.py`: placed f-string as a dict key — `e[f"{amount:.2f}"]` — caught quickly when explained
- Needed an extra REPL pass on the grouping pattern before the puzzle

### What Felt Solid
- Accumulator pattern clicked fast — drilled twice, wrote loop independently on second pass
- Explained `totals[e["category"]]` lookup correctly unprompted
- Applied `.capitalize()` and `:.2f` in `category_totals.py` without being prompted
- Wrote grouping loop from scratch without reference to the drilled version

### Where to Start Next Session
- Placement weak spot: no structural placement test this session — status unchanged (1/2 clean appearances needed to eliminate)
- Steps 4 and 5 complete — next: BUILD v0.1 of expense tracker
- Design the build step to surface placement weak spot (header, totals label, menu — all have placement decisions)
