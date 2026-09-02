# ROADMAP.md — Basics Reboot (Reactivation)

## The Point
Knock the rust off the core fundamentals and **get the daily coding rhythm back**.
After ~2 months away, a ground-floor assessment (S33) showed the *logic* is intact —
the misses were a few specific, repeating ideas, and each one clicked the instant
Dustin saw it run. **This is reactivation, not remedial.** Rust burns off fast.

**Why this track, why now:** the Scripting track went dry and daily practice
stalled. The old **puzzle format** (one concept → REPL drill → struggle-through
puzzle → commit) is what had Dustin coding every day. So we're returning to that
format and pointing it straight at the fundamentals that came up shaky. Momentum
is the asset we're protecting — a "correct" roadmap that goes untouched teaches
nothing.

**Still pure Python, stdlib only.** No third-party libraries. REPL + small puzzle
files, same as the original roadmap that worked.

---

## Assessment findings (S33) — what we're patching
Solid ✅: variables & types, reassignment, if/else, function *calls*, list/dict
access, `len()`, and the *intuition* for `return` vs `print`.

Gaps 🔧 (front-loaded below, worst first):
1. **Zero-based indexing** — the big one, missed twice (`"hello"[1]`, `range(3)`).
   Python counts from **0**; first item is position `0`.
2. **String building** — `"cat" + "dog"` → `catdog`; Python never adds a space for you.
3. **String methods** — `.upper()` etc. — the `object.method()` shape was unfamiliar.
4. **Method-call syntax** — `nums.append(40)`, not `append(40)`. Same shape as #3,
   so they close together.

---

## How to Read This
- **Learn** steps: REPL drill + puzzle. Both checked before moving on.
- At session start, scan for the first unchecked box.
- **Pace:** thorough over speed (Dustin's standing rule). Full REPL drills before
  every concept, explain-backs that actually probe, no advancing until solid.
- Every finished puzzle → its own file in `puzzles/`, commit + push, update
  `PUZZLE_INDEX.md`. Confirm each method is in `DRILLS.md`/`REFERENCE.md` first;
  if not, drill it and add it.

---

## Steps

### 1. Zero-based indexing — grab items by position
*Teaches: strings and lists are indexed from 0; `[0]` is first, `[-1]` is last*
- [x] REPL/drill — index a string and a list; predict `"python"[0]`, `[-1]`, `range(3)` as a list
- [x] Puzzle — `first_last.py`: print the first and last character of any word

### 2. Slicing — grab a *range* of items
*Teaches: `[start:end]` (end is excluded), on both strings and lists*
- [x] REPL/drill — `"python"[0:3]`, `"python"[2:]`, `nums[1:3]`; predict each first
- [x] Puzzle — `slice_it.py`: from a word, print the first 3 letters and the last 2

### 3. Building strings — glue and format
*Teaches: `+` just concatenates (no auto-space); f-strings for clean building*
- [x] REPL/drill — `"cat" + "dog"`, `"cat" + " " + "dog"`, `f"{name} is {age}"`
- [x] Puzzle — `greeting.py`: from a name variable, print `Hello, <name>!` two ways (`+` and f-string)

### 4. String methods — transforming text
*Teaches: the `object.method()` pattern; `.upper()`, `.lower()`, `.strip()`, `.replace()`*
- [x] REPL/drill — `"python".upper()`, `"  hi  ".strip()`, `"a,b".replace(",", "-")`
- [x] Puzzle — `shout.py`: take a messy string and print it clean + uppercase

### 5. List methods — changing a list
*Teaches: `.append()`, `.remove()`, reassign vs. in-place; reuses `object.method()` from #4*
- [x] REPL/drill — build a list, `.append()`, `.remove()`, check `len()` after each
- [x] Puzzle — `todo.py`: start with a list, add two items, remove one, print the result

### 6. Loops — repeating with a counter and over a list
*Teaches: `for x in list`, `range(n)` starts at 0, looping with an index*
- [x] REPL/drill — `for i in range(3)`, `for item in nums`; predict output before running
- [x] Puzzle — `count_up.py`: print each item in a list with its position number

### 7. Conditionals — deeper
*Teaches: `if`/`elif`/`else`, comparisons, `in` for membership*
- [x] REPL/drill — `5 > 3`, `"a" in "cat"`, an `if`/`elif`/`else` chain
- [x] Puzzle — `grade.py`: given a score, print a letter grade using `if`/`elif`/`else`

### 8. Dicts — deeper
*Teaches: add/update a key, check membership, loop over keys/values*
- [ ] REPL/drill — add a key, update a value, `for k in d`, `d.items()`
- [ ] Puzzle — `tally.py`: count how many times each letter appears in a word (accumulator dict)

### 9. Functions — write your own
*Teaches: parameters vs. arguments, `return` vs `print` (sharpen the S33 intuition), calling your own function*
- [ ] REPL/drill — define a function, `return` a value, store it in a variable, `print` it
- [ ] Puzzle — `helpers.py`: write a function that takes a word and returns it reversed

### CAPSTONE — tie it together
*Prereqs: steps 1–9. One small puzzle that uses indexing, a loop, a dict, and a function.*
- [ ] `word_stats.py`: given a word, print its length, first & last letter, uppercase
      version, and a letter-frequency tally — built from a function you wrote

---

## After the Reboot
- Return to the **Scripting track** (`roadmaps/ROADMAP_scripting_PAUSED.md`) once the
  daily rhythm is back and the fundamentals feel automatic — resume at Step 4.
- Or pick the next fundamentals gap the reboot surfaces and keep the puzzle rhythm going.

## Parked (set aside on purpose)
- Scripting / vault tools — `roadmaps/ROADMAP_scripting_PAUSED.md` (resume at Step 4)
- OOP / writing your own classes — `roadmaps/ROADMAP_oop_PAUSED.md`
- GUI Expense Tracker (CustomTkinter) — `roadmaps/ROADMAP_expense_gui_PAUSED.md`
- Flask web walkthrough — `roadmaps/ROADMAP_flask_walkthrough.md`
