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
