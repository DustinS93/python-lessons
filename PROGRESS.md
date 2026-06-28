## Session 26 — 2026-06-27

### What We Covered
- Opener: dict/list access from memory — wrote `totals[e["category"]] = totals[e["category"]] + e["amount"]` COLD, no peeking (the fluency gap is closing)
- REPL drill: function name vs call — `say_hi` (object) vs `say_hi()` (runs) vs storing `x = say_hi` then `x()`
- Step 4 — callbacks: `command=on_click` (no parens = pass the function as a value, called later on click)
- `.configure(text=...)` to update a widget after creation; `global count` in a callback (scope trap → UnboundLocalError)
- Debugging: a crashing callback leaves the window running but prints the error to the TERMINAL — caught `NameError` (counter vs count) by looking there
- Step 5 — entry input: `CTkEntry`, `.get()` reads typed text as a string; greet via f-string in a label

### Puzzles Completed
- `puzzles/click_counter.py` (GUI Step 4: callback increments a label)
- `puzzles/greeter_gui.py` (GUI Step 5: entry → .get() → f-string greeting)

### Vocabulary Introduced
- callback (now used, not just named)

### What He Struggled With
- Confused creating a widget with reading one — callback made a NEW empty CTkEntry then `.get()` on it (always empty); also a duplicate stray entry
- Widget-vs-value: tried `name = name.get()`, clobbering the widget + re-triggering the scope trap
- Froze on writing the f-string into `.configure(text=...)` despite knowing f-strings
- Explain-back: said callback "stores the entry" — meant the TEXT from `.get()`, not the widget

### What Felt Solid
- Dict-access line written cold from memory — fluency gap nearly closed
- Function name-vs-call drill: all three predictions right
- Named the scope fix (`global count`) and the no-parens reason unprompted
- Observed on his own that the GUI runs from the terminal and `print()` lands there

### Where to Start Next Session
- Step 6: updating the display dynamically (`.configure`, building output strings) — last step before BUILD v0.1
- Placement: clean & unprompted both puzzles this session (widgets before mainloop, mainloop last) → streak 0 → 1
- Reinforce widget (the box) vs value (the string from `.get()`) — surfaced twice today
- Keep nudging: RUN and read the terminal before theorizing (paid off catching the NameError)
