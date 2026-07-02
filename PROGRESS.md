## Session 29 — 2026-07-01

### What We Covered
- REPL warm-up: list methods (`.append()`, `len()`, for loop) — feeds into class-holds-a-list
- Re-confirmed `self` = instance not class (slipped in S28 explain-back — clean this session)
- Stretch class: `Playlist` — `__init__` takes `name`, stores `self.songs = []`; `add_song(title)`, `show()` (for loop), `length()`
- Two kinds of `__init__` setup: data that varies per object (parameter) vs data that's always the same starting state (created fresh inside)
- Method as a printer: `show()` prints internally, caller doesn't wrap in `print()`
- Design principle reinforced: methods receive data via parameter, don't call `input()` internally

### Puzzles Completed
- `puzzles/playlist.py` (Playlist class: `__init__`, `add_song(title)`, `show()`, `length()`)

### Vocabulary Introduced
- (none new — reinforced: attribute, self, instance, method vs parameter)

### What He Struggled With
- Method-vs-parameter again: used `songs` as a parameter in `__init__` (should be `name`); moved `title` around without putting it in the `def` line
- `input()` inside `add_song` — kept drifting back to it despite the design principle from S28
- Backwards assignment (`name = self.name` instead of `self.name = name`) — one-off slip
- `self.songs()` — put parens on an attribute (list is not callable)
- Chained assignment confusion (`songs = self.songs = []`)

### What Felt Solid
- `self.attr` read/write inside methods — clean all session (no bare names, no globals)
- `self` = instance not class — confirmed correctly at session open and held
- Read every error himself and diagnosed it (TypeError positional args, NameError)
- Understood the "two kinds of init setup" distinction at explain-back
- `show()` as a printer (no return needed) — got it after seeing the duplicate output

### Where to Start Next Session
- Method that calls another method on the same object (`self.method()` inside a method)
- Consider another class rep from scratch before introducing method-calls-method
- Method-vs-parameter still the recurring trip-up — design next puzzle to surface it
- Check ROADMAP.md for next step
