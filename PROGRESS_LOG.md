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
