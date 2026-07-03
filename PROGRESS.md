## Session 30 — 2026-07-02

### What We Covered
- Roadmap pivot: parked OOP (understood fundamentally) → new **Scripting track** (terminal + Obsidian-vault tools, stdlib only)
- Set capabilities/limits model for vault scripting; designed builds (tag finder, empty-note report, tag MOC generator, vault stats)
- Set standing pace rule: **thorough over speed**
- Step 1 — `sys.argv`: running a script from the terminal, reading command-line arguments
- REPL vs script: a script only outputs what you explicitly `print()`; bare expressions evaluate silently
- `argv` is a list built fresh each run; slot 0 = script name, args split on spaces, quotes group into one item, no memory between runs

### Puzzles Completed
- `puzzles/greet.py` (reads name from `sys.argv[1]`, prints greeting — first script run from the terminal, not the REPL)

### Vocabulary Introduced
- script, command-line argument, `sys.argv`, shell/terminal, MOC (Map of Content)

### What He Struggled With
- REPL vs script vs shell: typed script code at the `>>>` prompt; copied bare REPL lines into the file → printed nothing (no `print()`)
- Assumed `argv` "remembered" a word between runs (stateful assumption) — corrected: each run is a blank slate
- Double space from `print(a, b)` comma auto-space + a trailing space in the text

### What Felt Solid
- Read every error himself and corrected each misconception once he saw the real output
- Explain-back clean: why a bare expression prints nothing; why the name is `argv[1]` not `argv[0]`
- Sharp product instincts designing the scripting roadmap

### Where to Start Next Session
- ROADMAP Step 2: read a file whose path comes from `sys.argv[1]` → `wordcount.py`
- Point all scripts at his **copy vault**
- Watch: REPL vs script vs shell (new context-juggling for scripting) — reinforce which prompt is which
