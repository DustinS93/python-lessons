# ROADMAP.md — Core Python: Object-Oriented Programming (OOP)

## The Point
Get genuinely strong at **pure Python** — no libraries. The current focus is
**writing your own classes** (OOP): the biggest concept-jump in Python and the
thing that makes all the library code Dustin's been *using* (`CTk`, `Flask`)
finally make sense from the inside.

**No libraries.** Everything here runs in plain `python3` — REPL drills and
`.py` files in `puzzles/` and `projects/`, exactly like the CLI work before the
GUI/Flask detours.

**Why OOP now:** Dustin asked "what *is* `customtkinter.CTk()`?" and bumped into
classes everywhere. He's ready to build his own. Started Session 27 (class,
`__init__`, `self`) — needs several more passes to feel automatic.

---

## How to Read This
Same format as always:
- **Learn** steps: REPL drill + puzzle. Both checked before moving on.
- **Build** is the milestone — a running pure-Python program.
- At session start, scan for the first unchecked box.

---

## Steps

### 1. Classes, objects, methods, `self` — the foundation
*Teaches: `class`, instantiating with `()`, methods, `self` = "this object"*
- [x] REPL drill — `Dog` class; `self` is the instance not the class (`d.who_am_i() == d`)
- [x] Puzzle — `expense_class.py` (an `Expense` class with `__init__` + a `summary()` method)
- [ ] **Reps (Session 28 opener):** write 1–2 small classes cold (e.g. `Dog` with a name + `describe()`), rebuilding `__init__`/`self` from scratch until it's automatic. *self.attr access inside methods is the watch point.*

### 2. Many objects + a list of objects
*Needed for: the real payoff — collections of your own objects*
*Teaches: making several instances, storing them in a list, looping to call a method on each*
- [ ] REPL drill — make a list of 3 objects, loop and call a method on each
- [ ] Puzzle — `team_roster.py` (a list of `Player`/`Pet` objects; loop prints each one's summary)

### 3. Methods that change the object
*Needed for: objects that do more than describe themselves*
*Teaches: a method that updates `self.something` (mutating state)*
- [ ] REPL drill — a method that increments a counter attribute on `self`
- [ ] Puzzle — `bank_account.py` (deposit/withdraw methods change `self.balance`)

---

### BUILD — Expense Tracker, OOP edition (CLI, no libraries)
*Prerequisites: steps 1–3. Reuses logic Dustin already knows, restructured around a class.*
- [ ] An `Expense` class (desc, category, amount) with a `summary()` method
- [ ] Add expenses as objects into a list
- [ ] Loop the list to print all summaries
- [ ] A total, and totals per category, computed from the objects
- [ ] Runs in the terminal; committed to GitHub

---

## After OOP
- Comprehensions (list/dict) and cleaner idioms
- Possibly: save/load the objects to a file (ties OOP back to file I/O he knows)
- Reassess web vs. desktop later — only if/when he wants a project with a UI again

## Parked (libraries — set aside on purpose)
- GUI Expense Tracker (CustomTkinter) — `roadmaps/ROADMAP_expense_gui_PAUSED.md`
- Flask web walkthrough (a tour, explored not learned) — `roadmaps/ROADMAP_flask_walkthrough.md`
