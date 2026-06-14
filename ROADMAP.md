# ROADMAP.md — CLI Shopping List Manager

## The Project
A command-line shopping list app. The user can add items, view the list,
mark items done, and save to a file so the list persists between runs.

**Project file:** `projects/shopping_list.py`

---

## How to Read This

Each step is either a **Learn** step or a **Build** step.

- **Learn** steps have two checkboxes: drilled in REPL and puzzle completed.
  Both must be checked before moving to the next step.
- **Build** steps are milestones where you write a working version of the
  project using what you've learned. The app should run after every build step.
- Check off boxes as you go. At session start, scan for the first unchecked box — that's where we are.

---

## Steps

### 1. `print` vs `return`
- [x] Drilled in REPL
- [x] Puzzle: `describe_pet.py`

### 2. Parameters and arguments
- [x] Drilled in REPL
- [x] Puzzle: `describe_pet.py`

### 3. Default parameters
- [x] Drilled in REPL
- [x] Puzzle: `describe_pet.py`

### 4. Functions calling functions / passing return values as arguments
- [x] Drilled in REPL
- [x] Puzzle: `bill_splitter.py`, `temp_converter.py`

### 5. Type conversion — `str()`, `int()`, `float()`
- [x] Drilled in REPL
- [x] Puzzle: `temp_converter.py`

### 6. Conditionals — `if` / `elif` / `else`
- [x] Drilled in REPL
- [x] Puzzle: `grade_checker.py`

### 7. `input()` and `int(input())`
- [x] Drilled in REPL
- [x] Puzzle: `ticket_price.py`

### 8. Scope — local vs global variables
- [x] Drilled in REPL
- [x] Puzzle: `the_vault.py`

### 9. Lists — creating, indexing `[0]` `[-1]`, `len()`
- [x] Drilled in REPL
- [x] Puzzle: `the_shopping_list.py`, `the_countdown.py`

### 10. `for` loops — counter pattern, combining with conditionals
- [x] Drilled in REPL
- [x] Puzzle: `the_shopping_list.py`, `the_countdown.py`, `the_grade_book.py`

---

### 11. List methods — `.append()`, `.remove()`, `.pop()`
*Needed for: adding and removing items from the shopping list*
- [x] Drilled in REPL
- [x] Puzzle: `grocery_cart.py`

### 12. `while` loops — `while True`, `break`
*Needed for: keeping the app running until the user decides to quit*
*Note: basic `while condition` was covered in session 7. This step is the `while True / break` pattern specifically — different mechanic, not yet drilled.*
- [x] Drilled in REPL
- [x] Puzzle: `menu_loop.py`

---

### BUILD v0.1 — Working core (no file saving yet)
*Prerequisites: steps 1–12 complete*
- [x] App runs and shows a menu: `[1] Add item  [2] View list  [3] Quit`
- [x] User can add items — stored in a list with `.append()`
- [x] User can view the full list — numbered with a for loop
- [x] Quit exits the program cleanly
- [x] Menu loops with `while True`, `break` on quit

---

### 13. Modifying list items — `list[i] = value`
*Needed for: marking items as done*
- [x] Drilled in REPL
- [x] Puzzle: `mark_done.py`

### 14. Storing a return value in a variable — `result = function()`
*Needed for: clean, readable project code*
- [x] Drilled in REPL
- [x] Puzzle: `name_badge.py`

---

### BUILD v0.2 — Mark items done
*Prerequisites: steps 13–14 complete*
- [ ] Menu gains option: `[4] Mark item done`
- [ ] User picks an item by number
- [ ] Done items display with a marker — e.g. `[x] eggs`
- [ ] App still loops, all previous features work

---

### 15. File I/O — reading and writing files
*Needed for: saving the list so it survives closing the app*
- [ ] Drilled in REPL
- [ ] Puzzle

---

### BUILD v0.3 — Complete project
*Prerequisites: step 15 complete*
- [ ] On startup, load existing list from `shopping_list.txt` if it exists
- [ ] On quit, save current list to `shopping_list.txt`
- [ ] App is fully functional: add, view, mark done, persist across runs
- [ ] Committed to GitHub as first real project

---

## Stretch (after v0.3)
These are not required for the project but are natural next steps:
- Dictionaries — store items as `{"name": "eggs", "done": False}` instead of two lists
- Refactor v0.3 using dictionaries
- Error handling — what if the user types a letter instead of a number?
