## Session 1 — 2026-06-04

### What We Covered
- `print` vs `return` — print displays to screen, return hands a value back to the caller
- Parameters vs arguments — parameters are placeholders in the definition, arguments are values passed at call time
- Default parameters — must come after parameters without defaults; used as fallback when no argument is passed
- Passing multiple arguments to a function
- String concatenation inside return statements (spacing matters)

### Puzzles Completed
- `puzzles/describe_pet.py` — function that takes `name` and optional `animal` (default: "dog"), returns a sentence

### Vocabulary Introduced
- parameter
- argument
- default parameter
- return value

### What He Struggled With
- Passing string arguments (passed bare words instead of quoted strings — "not defined" error)
- Default parameter syntax — initially set the default as a variable outside the function instead of inside the `def` line
- String spacing in concatenation

### What Felt Solid
- `print` vs `return` distinction clicked quickly
- Understood why default parameters must come after non-default ones unprompted
- Read and interpreted error messages himself before asking

### Notes for Next Session
- Cover passing multiple arguments explicitly in drills before the puzzle — Dustin flagged this was missing this session
- He's self-aware about gaps, good instinct for debugging
- Pick up with: more function practice or introduce scope (local vs global variables)

---

## Session 2 — 2026-06-04

### What We Covered
- Type conversion drills: `str()`, `int()`, `float()`
- `int("7.5")` raises ValueError — must go `float()` first, then `int()`
- `int()` truncates, does not round
- Why `"string" + 42` fails — can't concatenate str and int
- REPL "print" explained — the P in REPL, not Python's `print()`
- Functions calling functions with type conversion in the return string

### Puzzles Completed
- `puzzles/temp_converter.py`

### Vocabulary Introduced
- truncation
- REPL (Read, Evaluate, Print, Loop)

### What He Struggled With
- Minor: typo and missing " F" in format string — caught on review

### What Felt Solid
- Type conversion drills — got `int(float("7.5"))` unprompted
- Recognized why `str()` was needed without being told
- Connected REPL behavior to the acronym himself

### Notes for Next Session
- Type conversion is solid — ready to move on
- Next: introduce scope (local vs global variables), or conditional logic (`if`/`else`)

---

## Session 3 — 2026-06-04

### What We Covered
- Conditionals: `if`, `elif`, `else`
- `>` vs `>=` — strictly greater than vs greater than or equal
- Python checks conditions top to bottom and stops at first true match
- No output when condition is false and no `else` — not an error
- Applied `str()` in a puzzle without being prompted

### Puzzles Completed
- `puzzles/grade_checker.py`

### Vocabulary Introduced
- conditional
- `elif`

### What He Struggled With
- Nothing significant — thought through the two-function design himself before writing

### What Felt Solid
- `if`/`elif`/`else` structure clicked immediately
- Reasoned through passing a return value as an argument unprompted
- Used `str()` correctly without a reminder

### Notes for Next Session
- Conditionals are solid
- Next: scope (local vs global variables) OR introduce `input()` to make programs interactive

---

## Session 4 — 2026-06-05

### What We Covered
- `input()` — prompts user, pauses program, returns a string
- `input()` always returns a string even if user types a number
- `int(input())` — wrapping input to convert at the source
- Redundant conditions in `elif` — if first `if` fails, later conditions are already implied
- Converting once vs converting repeatedly inside conditionals

### Puzzles Completed
- `puzzles/ticket_price.py`

### Vocabulary Introduced
- (none new)

### What He Struggled With
- Tried to convert in the parameter definition — good instinct, wrong place

### What Felt Solid
- Knew immediately that `input()` returns a string
- Recognized the redundant `>= 13` check himself
- Figured out `int(input())` pattern on his own

### Where to Start Next Session
- `input()` is solid
- Next: scope (local vs global variables)

---

## Session 5 — 2026-06-05

### What We Covered
- Scope: local vs global variables
- Local variables only exist inside the function where they're defined
- Global variables are visible everywhere, including inside functions
- Same variable name in two scopes — function uses its own local copy
- Function definition order doesn't matter, only call order does
- `return` vs `print` inside functions — return hands a value back, print just displays

### Puzzles Completed
- `puzzles/the_vault.py`

### Vocabulary Introduced
- scope
- local scope
- global scope

### What He Struggled With
- Initially used `print` inside function + `print(lock())` outside — got `None`, reasoned through it himself

### What Felt Solid
- Immediately understood why `NameError` appeared when accessing local variable outside function
- Correctly predicted global variable accessible inside function
- Understood `return` vs `print` distinction quickly once he saw the `None`

### Where to Start Next Session
- Scope is solid
- Next: `global` keyword OR lists/loops revisit OR introduce more complex function patterns

---

## Session 6 — 2026-06-05

### What We Covered
- Lists: creating, indexing with `[0]`, `[-1]`, `len()`
- Negative indexing — `-1` is always the last item
- `for item in list` loop — loop variable is a temporary name, can be anything
- Loop counter pattern — variable before loop, increment inside loop
- `return` inside a loop exits the entire function immediately
- Parameter names are arbitrary — what matters is consistency inside the function

### Puzzles Completed
- `puzzles/the_shopping_list.py`
- `puzzles/the_countdown.py`
- `puzzles/the_grade_book.py`

### Vocabulary Introduced
- index
- negative index

### What He Struggled With
- `number = +1` vs `number = number + 1` — subtle distinction, caught himself
- Hardcoded counter instead of `len()` — corrected when prompted
- Initially used `return` inside loop — understood why it was wrong once reminded what `return` does

### What Felt Solid
- Loop variable naming clicked immediately — tested it himself
- Combining loops with conditionals in `the_grade_book.py` — wrote it cleanly
- Knew when to drop `print()` wrapper vs when to use `return`

### Where to Start Next Session
- Lists and loops are solid
- Next: list methods (`append`, `remove`, etc.) OR introduce `while` loops OR step up puzzle complexity

---

## Session 7 — 2026-06-06

### What We Covered
- Keyword arguments — passing arguments by name, order doesn't matter
- `while` loops — run based on a condition, not a fixed list
- Infinite loops — what causes them and how to avoid (must update the condition inside the loop)
- Code after a `while` block runs once when the loop ends
- Converting `int()` once at the call site instead of repeatedly inside the function

### Puzzles Completed
- `puzzles/while_countdown.py`

### Vocabulary Introduced
- keyword argument

### What He Struggled With
- `return` inside a loop again — caught it with a nudge back to prior puzzles
- Tried putting `int()` in the `def` line — clarified that parameter names must be plain names
- Placed `print("Blast Off!")` outside the function initially — understood indentation fix quickly

### What Felt Solid
- Guessed infinite loop correctly without running it
- Understood why condition is checked before the loop body runs
- Converted `int()` once at call site once pointed in the right direction

### Where to Start Next Session
- `while` loops solid
- Next: list methods (`append`, `remove`, `pop`, `in`) OR a harder puzzle combining while + lists

---

## Session 8 — 2026-06-07

### What We Covered
- List methods: `append`, `pop`, `remove`, `in`
- `pop()` removes and returns the last item — return value can be caught in a variable
- `remove(item)` removes by value, not by index
- `in` returns a boolean — no need for `== True`
- `return` inside a loop exits the entire function — "not found" return goes outside the loop
- `for...else` is valid Python but not the intended pattern — cleaner without `else`
- `input()` inside a `def` line runs at definition time, not call time (recurring)
- Hardcode starter data when a puzzle needs a populated list — don't rely on `input()` for setup

### Puzzles Completed
- `puzzles/grocery_cart.py`

### Vocabulary Introduced
- (none new)

### What He Struggled With
- `input()` placed inside `def` line again — same pattern as `int()` in sessions 4 and 7
- `if item in cart == True` — removed `== True` once reminded what `in` returns
- `item in i` vs `i == item` in find_item — flipped twice before correcting
- Cart population: "starts as empty list" without clear setup instructions caused confusion

### What Felt Solid
- Caught that `remove_last` was emptying the cart before `remove_item` ran
- Understood `pop()` returns the removed item after one nudge
- `return` outside the loop in `find_item` — got it right after the session-opening drill
- Explained all four methods accurately at session end

### Where to Start Next Session
- List methods solid
- Next: `while` loop + `append` to build a multi-item cart (natural follow-on from today)
- Surface `return` inside loop again — not yet eliminated (needs 2 consecutive clean appearances)

---

## Session 9 — 2026-06-08

### What We Covered
- `return` inside a loop — targeted drill, clarified it's not an `else` branch, just the next line in sequence after the loop finishes
- `while` loop + `append` + `input()` — wired together in a self-contained function
- Self-contained function: no parameters, creates its own data (`cart = []`, `item = input()`) internally
- Redundant `break` — while condition handles exit on its own

### Puzzles Completed
- `puzzles/grocery_cart_v2.py`

### Vocabulary Introduced
- (none new)

### What He Struggled With
- `return` inside the loop again — placed it inside the while block before catching it when prompted with the drill connection
- Didn't know how to make a function self-contained — tried passing `cart` and `item` as parameters from outside
- `NameError` when removing parameters but not updating the function call

### What Felt Solid
- Connected `return` placement to the session-opening drill after being nudged
- Understood while loop exits naturally — no `break` needed
- Self-contained function concept explained clearly at session end

### Where to Start Next Session
- `return` inside loop: surfaced again (session 9) — still not eliminated, needs 2 consecutive clean unprompted appearances
- Next puzzle should surface `return` inside a loop again naturally
- Consider: dictionary basics OR `for` + `while` combination

---

## Session 10 — 2026-06-10

### What We Covered
- `return` inside a loop — targeted opening drill (3+ weak spots threshold)
- `for` + `while` combination — `while` inside `for`, controlling inner loop independently
- Initializing `answer = ""` before a while loop so it always runs at least once
- Dead code — line after `return` never executes
- Placement: what belongs inside while vs outside, and why

### Puzzles Completed
- `puzzles/inventory_check.py`

### Vocabulary Introduced
- (none new)

### What He Struggled With
- Placement — figuring out what goes inside the while vs before it, and in what order (recurring weak spot)
- Quit logic: placed `if quit` before the while loop first — had to be guided to see it never triggered inside the loop

### What Felt Solid
- `return` exits the whole function even when nested inside two loops — stated correctly in drill and at session end
- `while answer != "yes"` — understood to check a value directly, not a bool flag
- Dead code — spotted immediately once pointed at it

### Where to Start Next Session
- `return` inside loop: surfaced in session 10 puzzle — needed guidance on structure, not yet eliminated
- Placement weak spot: confirmed again — design next puzzle to surface it
- Next concept: dictionary basics (was planned, got bumped — now properly drilled first before use)

---

## Session 11 — 2026-06-11

### What We Covered
- `return` inside a loop — targeted opening drill (3+ weak spots threshold)
- Dictionary basics: creating, accessing by key, adding keys, updating keys
- `KeyError` — accessing a key that doesn't exist
- `len()` on a dictionary
- `.keys()` — returns all keys in a dictionary
- Setting a variable before building a dictionary, then using it as a value

### Puzzles Completed
- `puzzles/student_record.py`

### Vocabulary Introduced
- key
- value
- key-value pair

### What He Struggled With
- `==` vs `=` — used comparison instead of assignment inside `if` block
- Placement: put `return passed` inside the `if` block, exiting before the dictionary was built
- Hardcoded dictionary value instead of using the variable (`45` instead of `grade`)

### What Felt Solid
- `return` inside a loop drill — clean, explained correctly with no guidance
- Understood `passed` is just a variable — dictionary reads it, no return needed
- Spotted `==` vs `=` issue himself once prompted to look at the line
- Understood why lists use index and dictionaries use keys at session end

### Where to Start Next Session
- `return` inside loop: clean in opening drill — 1 of 2 consecutive clean appearances needed to eliminate
- Placement weak spot: surfaced again (return inside if block) — still recurring

---

## Session 12 — 2026-06-11

### What We Covered
- `return` inside a loop — opening drill, 2nd consecutive clean appearance (eliminated)
- `None` — Python's "nothing" value, always capital N. REPL suppresses it; `print()` shows it
- Case sensitivity — `None` vs `none`, Python distinguishes uppercase from lowercase everywhere
- `while True / break` — loops forever until `break` fires; use when no value exists to check at loop start
- `break` vs `return` — `break` exits the loop, `return` exits the entire function
- BUILD v0.1 — first working version of the shopping list app

### Puzzles Completed
- `puzzles/menu_loop.py`
- `projects/shopping_list.py` (BUILD v0.1)

### Vocabulary Introduced
- `None`
- case-sensitive
- `break`

### What He Struggled With
- Used `return` instead of `break` in menu puzzle — needed reminder of the distinction
- REPL showing nothing for `None` return — confused about whether function ran

### What Felt Solid
- `while True` rationale — explained correctly that no condition exists yet at loop start
- `shopping_list = []` outside the loop — caught the reset problem when asked
- BUILD v0.1 structure clean — loop, list, append, numbered view, break on quit all correct

### Where to Start Next Session
- `return` inside loop: ELIMINATED — 2 consecutive clean appearances (sessions 11 and 12)
- Placement weak spot: still active — surfaced in menu puzzle (return vs break)
- Next: Step 13 — modifying list items `list[i] = value`, needed for marking items done (BUILD v0.2)

---

## Session 13 — 2026-06-12

### What We Covered
- List indexing review — `items[0]`, `items[-1]`, `len(items)` (opening drill, 2+ sessions ago)
- `list[i] = value` — modifying an item in place by index
- `"[x] " + items[i]` — prepending a string to mark an item done
- `int(input()) - 1` — converting 1-based user input to 0-based index
- Input validation — checking `choice < 1 or choice > len(items)` before updating
- `return` to exit early from a function on invalid input

### Puzzles Completed
- `puzzles/mark_done.py`

### Vocabulary Introduced
- (none new)

### What He Struggled With
- Condition logic: used `and` instead of `or` for invalid range check
- Update ran before the validation check — order was backwards initially

### What Felt Solid
- Caught `input()` inside function was wrong (parameter should come from caller)
- Caught `print(print_list(...))` printing `None` himself
- Fixed `<= 1` to `< 1` after testing edge case himself
- Order issue (check before update) — caught it when prompted, not fully unprompted yet

### Where to Start Next Session
- Placement weak spot: still active — surfaced again (check after update), caught when prompted
- Next: Step 14 — storing a return value in a variable (`result = function()`), needed for BUILD v0.2
- After Step 14: BUILD v0.2 — mark items done in the shopping list app
- Next: dictionary puzzle with input() and updating keys, or add a second dictionary concept (e.g. iterating over keys)

---

## Session 14 — 2026-06-13

### What We Covered
- Opening REPL drill: `.pop()` removes and returns the last item — value can be caught in a variable
- `result = function()` — storing a return value before using it
- REPL drills: `double(result)`, `message = add_greeting()`, direct vs stored return value
- Validation placement — check belongs in main code, not inside a helper function
- Puzzle: two clean functions, store-then-validate-then-act pattern

### Puzzles Completed
- `puzzles/name_badge.py`

### Vocabulary Introduced
- (none new)

### What He Struggled With
- Placement (x3 in one puzzle): validation inside `get_name()`, then `make_badge()` called before empty check, then `badge` stored outside the `else` block — each caught when prompted, none unprompted
- Recognized the tangling problem himself once asked about it (get_name returning "Name required", make_badge having to check for it)

### What Felt Solid
- REPL drills clicked fast — chained return values, doubled result, understood argument vs parameter unprompted
- Understood why two tangled functions is a problem once he saw it
- Final structure was clean: get → store → check → act

### Where to Start Next Session
- Placement weak spot: still very active — 3 separate placement mistakes in one puzzle (session 14), all caught when prompted
- Step 14 complete — both checkboxes done
- Next: BUILD v0.2 — mark items done in shopping list app

---

## Session 15 — 2026-06-14

### What We Covered
- Opening REPL drill: `list[i] = value` — modifying list items in place
- BUILD v0.2 confirmed complete — checked off in ROADMAP
- File I/O: `open()` modes (`"r"`, `"w"`, `"a"`), `with open() as f:`, `f.write()`, `f.read()`, `f.readlines()`, `.strip()`
- `\n` as escape sequence in code vs literal characters when typed as input
- Puzzle: `goal_saver.py` — write goal to file, read it back, return clean value
- `import os`, `os.path.exists()` — modules intro, what import does
- BUILD v0.3 complete — load from file on startup, save on quit

### Puzzles Completed
- `puzzles/goal_saver.py`
- `projects/shopping_list.py` (BUILD v0.3 — complete project)

### Vocabulary Introduced
- (none new)

### What He Struggled With
- Placement: `input()` inside `save_goal()`, `print()` inside `load_goal()` — caught when prompted
- Placement: multiple iterations to get read block correct in BUILD v0.3 — loop direction backwards (looping over shopping_list instead of contents), and method confusion
- Asked sharp questions unprompted about modules vs file object methods — good instinct

### What Felt Solid
- File I/O concepts clicked in drills — explained `"r"` vs `"w"` correctly at session end
- `import` and module vs file object distinction — understood after one explanation
- App works end to end: add, view, mark done, persist across runs
- Recognised `\n` vs typed `\n` after seeing the file contents

### Where to Start Next Session
- Placement weak spot: persistent — multiple errors across goal_saver and BUILD v0.3, all caught when prompted
- Project complete — CLI Shopping List Manager done, committed to GitHub
- ROADMAP stretch goals available: dictionaries refactor, error handling
- Or define a new roadmap project

---

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

---

## Session 17 — 2026-06-15

### What We Covered
- Opening REPL drill: dictionary basics — accessing, updating, adding keys, `.keys()`, `len()`
- `try/except ValueError` — catching errors from bad user input instead of crashing
- `not in range(len(list))` — checking for out-of-range input
- Why logic inside `try` block matters — anything after a failed line is skipped, variables never assigned

### Puzzles Completed
- `puzzles/number_picker.py`

### Vocabulary Introduced
- (none new)

### What He Struggled With
- `if choice != 0 or 1 or 2` — thought this checked all three values; learned `or 1` is always truthy
- Placement: `choice = choice - 1` and conditionals initially outside `try` block — caught it himself mid-puzzle after NameError
- `try/except` explanation at session end was slightly incomplete — named the what but not the why on placement

### What Felt Solid
- Diagnosed NameError himself: "choice only gets assigned if the try block succeeds" — correct, unprompted
- Used `range(len(grocery_list))` independently — cleaner than a hardcoded list
- Simplified `if/elif` chain to `grocery_list[choice]` unprompted

### Where to Start Next Session
- Placement weak spot: surfaced again — but Dustin caught it himself this time (NameError → diagnosis → fix without being told). Progress.
- Next: error handling in shopping_list.py (apply try/except to the real project), or new puzzle concept
- `try/except` is new — worth one more puzzle before moving on

---

## Session 18 — 2026-06-16

### What We Covered
- Opening REPL drill: chaining return values — `result = function()`, passing return values as arguments
- `input_validator.py` — second `try/except ValueError` puzzle, range checking 1–10
- `IndexError` — raised when accessing a list index out of range
- Nested `try/except` — inner `except IndexError` inside outer `except ValueError`
- Applied error handling to `shopping_list.py` — both `ValueError` (bad menu input) and `IndexError` (out-of-range item selection)

### Puzzles Completed
- `puzzles/input_validator.py`

### Vocabulary Introduced
- `IndexError`

### What He Struggled With
- Placed `if choice == 5:` inside `except IndexError` block — caught it after being pointed to the line numbers, not fully unprompted

### What Felt Solid
- Correct `except IndexError` syntax guessed unprompted from `ValueError` pattern
- Range check fix (`<= 10`) caught and applied himself
- Structural reasoning: knew choice 5 needed to be outside the inner try/except once spotted

### Where to Start Next Session
- Placement weak spot: surfaced again in shopping_list.py (choice 5 inside except block) — caught after a hint. Not a clean unprompted appearance. Still tracking.
- Error handling stretch goal in ROADMAP.md is complete — check off and decide next direction
- Next concept TBD: new roadmap topic or consolidation

## Session 18 — 2026-06-16

### What We Covered
- Opening REPL drill: chaining return values — `result = function()`, passing return values as arguments
- `input_validator.py` — second `try/except ValueError` puzzle, range checking 1–10
- `IndexError` — raised when accessing a list index out of range
- Nested `try/except` — inner `except IndexError` inside outer `except ValueError`
- Applied error handling to `shopping_list.py` — both `ValueError` (bad menu input) and `IndexError` (out-of-range item selection)

### Puzzles Completed
- `puzzles/input_validator.py`

### Vocabulary Introduced
- `IndexError`

### What He Struggled With
- Placed `if choice == 5:` inside `except IndexError` block — caught it after being pointed to the line numbers, not fully unprompted

### What Felt Solid
- Correct `except IndexError` syntax guessed unprompted from `ValueError` pattern
- Range check fix (`<= 10`) caught and applied himself
- Structural reasoning: knew choice 5 needed to be outside the inner try/except once spotted

### Where to Start Next Session
- Placement weak spot: surfaced again in shopping_list.py — caught after a hint, not unprompted. Still tracking.
- Start expense tracker roadmap: step 1 is `float`, nothing checked off yet
- After expense tracker, plan a Pygame or Tkinter roadmap (Dustin expressed interest)
