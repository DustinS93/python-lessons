## Session 22 — 2026-06-22

### What We Covered
- Opening REPL drill: grouping/accumulating with `dict.keys()` and `:.2f` (session 19/20 concept)
- File I/O REPL pass 1: saving a list of dicts to file — comma-separated values, `\n`, only values written
- File I/O REPL pass 2: `os.path.exists()` wrapping the load block, `return []` fallback
- Full round-trip: save → file → load → list of dicts with correct types
- `result = load_movies()` — storing a function's return value
- f-string single quotes inside double-quoted string

### Puzzles Completed
- `puzzles/movie_log.py`

### Vocabulary Introduced
- (none new)

### What He Struggled With
- `f.write()` takes one string argument — passed comma-separated pieces instead of concatenating
- `return load_movies` instead of `return loaded_movies` — returned the function, not the variable
- `os.path.exists` block floating outside any function — structural placement error, caught on review
- Two `with open` blocks inside `load_movies` — redundant, caught on review
- `"title:"` — colon inside the string key instead of as dict separator
- Rating as MPAA string ("R"/"G") instead of float

### What Felt Solid
- `lines = f.readlines()` explained correctly: "a list of strings, 1 for each line"
- Round-trip concept articulated well at session end
- `result` catches what `return` hands back — explained correctly unprompted
- `key not in dict` pattern explained correctly when asked

### Where to Start Next Session
- Placement weak spot: streak still 0 — `os.path.exists` block outside function, caught on review
- Next: BUILD v0.2 — add save on quit and load on startup to `expense_tracker.py`, plus `try/except` on amount input
