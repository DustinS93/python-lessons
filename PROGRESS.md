## Session 15 — 2026-06-14

### What We Covered
- Opening REPL drill: `list[i] = value` — modifying list items in place
- BUILD v0.2 confirmed complete — checked off in ROADMAP
- File I/O: `open()` modes (`"r"`, `"w"`, `"a"`), `with open() as f:`, `f.write()`, `f.read()`, `f.readlines()`, `.strip()`
- `\n` as escape sequence in code vs literal characters when typed as input
- Puzzle: `goal_saver.py` — write goal to file, read it back, return clean value

### Puzzles Completed
- `puzzles/goal_saver.py`

### Vocabulary Introduced
- (none new)

### What He Struggled With
- Placement: `input()` inside `save_goal()` instead of main code — caught when prompted
- Placement: `print()` inside `load_goal()` instead of `return` — caught when prompted, self-corrected after explanation

### What Felt Solid
- File I/O concepts clicked quickly — explained `"r"` vs `"w"` correctly at session end
- `with open()` pattern — refactored both functions correctly without help
- Understood why `"r"` and `"w"` are fixed strings, not conventions
- Caught `\n` in code vs `\n` typed as input — understood after seeing the file

### Where to Start Next Session
- Placement weak spot: still active — 2 placement errors in puzzle, both caught when prompted
- Step 15 complete — both checkboxes done
- Next: BUILD v0.3 — load list from file on startup, save on quit
