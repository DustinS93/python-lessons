## Session 16 — 2026-06-14

### What We Covered
- System compression: DRILLS.md restructured (Puzzle Index, Active Concepts, Ingrained), CLAUDE.md updated
- REPL drills: list of dicts, accessing dict fields in a loop, `.pop(index)`, `str.split(",")`, bool from string comparison (`parts[1] == "True"`)
- Dictionaries refactor of shopping_list.py — items stored as `{"name": ..., "done": False}` instead of plain strings
- Added delete item option using `.pop(index)`
- File format: save as `name,done` per line, reconstruct on load with `.split(",")` and string comparison

### Puzzles Completed
- (none — project refactor session)

### Vocabulary Introduced
- (none new)

### What He Struggled With
- Load block indentation — new lines ended up outside the for loop, required multiple saves to fix
- `.pop([remove_item - 1])` — extra square brackets around the argument (didn't clear on first fix)
- Bracket placement in save line — `str(item["done": + "\n"]))` — closing bracket in wrong place

### What Felt Solid
- List of dicts pattern clicked fast in drills
- Save format: wrote `item["name"] + "," + str(item["done"]) + "\n"` correctly on first try after guidance
- Key insight at session end: storing data vs. display strings — articulated correctly unprompted

### Where to Start Next Session
- Active concepts needing more reps: list of dicts, `.pop(index)`, `str.split()`, file format for structured data
- Placement weak spot: still active — indentation errors with load block this session
- Consider a standalone puzzle using list-of-dicts and `.pop(index)` before moving to error handling
- Or: error handling stretch goal (what if user types a letter instead of a number?)
