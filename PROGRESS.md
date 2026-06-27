## Session 25 — 2026-06-26

### What We Covered
- Opener placement drill: `return` inside a for loop — predicted `10` and named the fix correctly (drill, not build)
- Decided next roadmap: rebuild Expense Tracker as a **GUI app** with **CustomTkinter** (modern look). Archived CLI roadmap → `roadmaps/ROADMAP_expense_tracker_cli.md`
- Step 1: installed customtkinter via `python3 -m pip`; built first window (CTk, title, geometry, mainloop)
- Discussed "multiple Pythons" (why `python3 -m pip`) and dependencies (darkdetect/packaging pulled in)
- Step 2: widgets — `CTkLabel`, `CTkButton`, `.pack()`; naming convention `CTk` + widget
- Taught self-discovery: `dir(customtkinter)`, `help()`, official docs
- Step 3: layout — `.grid(row, column)`, row=down/column=right, no pack/grid mixing

### Puzzles Completed
- `puzzles/my_first_window.py` (GUI Steps 1–2: window + label + button)
- `puzzles/layout_practice.py` (GUI Step 3: grid layout)

### Vocabulary Introduced
- library/package, third-party package, pip, dependency, GUI, event-driven programming, event loop / mainloop, widget, geometry manager, callback (named, not yet used)

### What He Struggled With
- Placement: stuffed widget lines INSIDE `mainloop()`'s parentheses — needed structural prompting to fix (not clean)
- row vs column swapped twice — fixed after a drawn grid scaffold
- Explain-back again needed scaffolding to get crisp (consistent pattern)

### What Felt Solid
- Strong analogical transfer: mapped grid/divs from CSS; intuited frames=divs before being taught
- Asked "where do I learn what that means" → then used `CTkEntry` unprompted via discovery
- Fixed the mainloop placement himself once pointed at the structure; described the event loop correctly

### Where to Start Next Session
- Step 4: callbacks (`command=`) — THE core event-driven concept; he already described it in explain-back
- Placement weak spot: appeared in build (widgets in mainloop), needed prompting → streak reset to 0
- Keep one puzzle per file (drifted into reusing my_first_window.py mid-session)
