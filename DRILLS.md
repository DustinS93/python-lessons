# DRILLS.md — Running Reference

## Vocabulary

| Term | Definition |
|---|---|
| parameter | The placeholder name in a function definition — `def greet(name)`, `name` is the parameter |
| argument | The actual value you pass when calling a function — `greet("Dustin")`, `"Dustin"` is the argument |
| default parameter | A parameter with a fallback value — `def greet(name, animal="dog")`. Must come after non-default parameters |
| keyword argument | Passing an argument by name when calling a function — `greet(greeting="Hi", name="Dustin")`. Order doesn't matter when you use the name |
| return value | The value a function hands back to the caller via `return`. Distinct from printing |
| truncation | Cutting off the decimal without rounding — `int(7.9)` gives `7`, not `8` |
| REPL | Read, Evaluate, Print, Loop — the interactive Python shell (`python3` in terminal) |
| conditional | A statement that runs code only if a condition is true — `if`, `elif`, `else` |
| elif | Short for "else if" — checks a new condition only if the previous one was false |
| scope | Where a variable exists and can be accessed |
| local scope | Inside a function — variables defined here only exist for the life of that function call |
| global scope | Outside all functions — visible everywhere in the file, including inside functions |
| index | The position of an item in a list. Starts at `0`. `list[0]` is the first item |
| negative index | Counting from the end of a list. `list[-1]` is always the last item |
| key | The label used to access a value in a dictionary — `person["name"]`, `"name"` is the key |
| value | The data stored at a key in a dictionary — `person["name"]` returns `"Dustin"`, the value |
| key-value pair | One entry in a dictionary — a key and its associated value, e.g. `"age": 30` |
| `None` | Python's built-in value for "nothing" — capital N. Returned by functions that don't explicitly return a value |
| `IndexError` | Raised when you access a list index that doesn't exist — e.g. `my_list[10]` on a 3-item list |
| case-sensitive | Python distinguishes uppercase from lowercase — `None` and `none` are completely different |

---

## Puzzle Index
Use this when Dustin is stuck on a concept — point him to the puzzle that covered it.

| Concept | Puzzle file(s) |
|---|---|
| print vs return, parameters, default params | `describe_pet.py` |
| functions calling functions, return values as args | `bill_splitter.py`, `temp_converter.py` |
| type conversion — str(), int(), float() | `temp_converter.py` |
| conditionals — if/elif/else | `grade_checker.py` |
| input(), int(input()) | `ticket_price.py` |
| scope — local vs global | `the_vault.py` |
| lists — creating, indexing, len(), for loops | `the_shopping_list.py`, `the_countdown.py` |
| for loop — counter pattern + conditionals | `the_grade_book.py` |
| list methods — .append(), .remove(), .pop(), in | `grocery_cart.py` |
| for loop + while loop on a list with input | `inventory_check.py` |
| while loop — while condition | `while_countdown.py` |
| while True + break (looping a cart) | `grocery_cart_v2.py` |
| while True + break (menu loop) | `menu_loop.py` |
| return inside a for loop | `check_password.py` |
| modifying list items — list[i] = value | `mark_done.py` |
| storing return value — result = function() | `name_badge.py` |
| file I/O — open, with, read, write, readlines, strip | `goal_saver.py` |
| dictionary basics — creating, accessing, updating | `student_record.py` |
| try/except ValueError — error handling on user input | `number_picker.py` |
| float — decimal numbers for money, storing return value | `tip_calculator.py` |

---

## Active Concepts
Verbose detail for concepts not yet fully ingrained. Update as new concepts are introduced.

### File I/O
- `open(filename, mode)` — opens a file. Modes: `"r"` (read), `"w"` (write, overwrites), `"a"` (append)
- `with open(filename, mode) as f:` — opens a file and closes it automatically when the block ends
- `f.write(text)` — writes a string to the file. Returns the number of characters written
- `f.read()` — reads the entire file as one string
- `f.readlines()` — reads the file as a list, one item per line. Each item includes the `\n` character
- `str.strip()` — removes whitespace and newline characters from both ends of a string. Use when reading lines from a file

### Modules
- `import os` — loads the `os` module (tools for interacting with the operating system)
- `os.path.exists(filename)` — returns `True` if the file exists, `False` if not

### Dictionaries
- Creating a dictionary: `person = {"name": "Dustin", "age": 30}`
- Accessing a value: `person["name"]` → `"Dustin"`
- Adding a key: `person["job"] = "developer"` — creates the key if it doesn't exist
- Updating a key: `person["age"] = 99` — overwrites the existing value
- `KeyError` — raised when you access a key that doesn't exist
- `len(dict)` — returns the number of key-value pairs
- `dict.keys()` — returns all keys in the dictionary

### List of Dictionaries
- A list can hold dicts as items: `items = [{"name": "eggs", "done": False}, {"name": "milk", "done": True}]`
- Access a field: `items[0]["name"]` → `"eggs"`
- Loop over and pull fields: `for item in items: print(item["name"], item["done"])`
- `.pop(index)` removes and returns the item at that position — the list holds dicts, so you get a dict back
- `str.split(",")` — splits a string on a delimiter, returns a list: `"eggs,False".split(",")` → `["eggs", "False"]`
- Reconstruct bool from file string: `parts[1] == "True"` — compares strings, result is a real boolean

### f-strings
- Prefix a string with `f` to make it an f-string: `f"Hello, {name}"`
- `{variable}` — inserts the variable's value directly into the string
- `{value:.2f}` — formats a float to always show 2 decimal places: `f"{2.5:.2f}"` → `"2.50"`
- The prefix `f` activates the f-string; the `f` in `:.2f` is a separate format spec for fixed-point decimals

### Error Handling
- `try/except` — wrap risky code in `try:`, catch the error in `except ErrorType:`
- `ValueError` — raised when a type conversion fails, e.g. `int("hello")`
- Code inside `except` only runs if that error occurs — otherwise skipped
- Code after the failing line inside `try` is also skipped when an error is raised

---

## Ingrained Concepts
Collapsed — covered and solid. No need to re-read at session start.

- **Functions:** def, parameters, arguments, default params, return, print vs return, functions calling functions, passing return values as arguments
- **Type conversion:** str(), int(), float(), int(float()), int(input())
- **Input:** input("prompt") — always returns a string
- **Conditionals:** if/elif/else — top to bottom, stops at first true condition
- **Scope:** local (inside function) vs global (outside). Same name in both scopes = local copy used inside the function
- **Lists:** create, index [0]/[-1], len(), for item in list, .append(), .remove(), .pop() (no args — removes last), item in list, list[i] = value
- **Loops:** for loop counter pattern, while condition, while True/break, break vs return vs continue
- **Storing return values:** result = function()
