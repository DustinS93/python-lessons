# DRILLS.md — Active Concepts

This is the session-start read. The rest of the reference system lives in:
- `VOCABULARY.md` — all terms (update immediately when new vocab comes up)
- `PUZZLE_INDEX.md` — concept → puzzle file map (consult when Dustin is stuck; update after each puzzle)
- `REFERENCE.md` — ingrained concepts + parked library notes (GUI, Flask)

Verbose detail for concepts not yet fully ingrained. When a concept is fully
ingrained, move it to `REFERENCE.md` as a one-line summary.

---

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
- `os.listdir(folder)` — returns a **list of strings**, the names inside `folder`. Names only, no path attached (`'greet.py'`, not `'puzzles/greet.py'`). Lists **everything** — files AND subfolders — with no filtering; you filter yourself — NEW S31
- `name.endswith(".md")` — a **boolean** test on a string: `True` if it ends with that text. Use in an `if` to keep only certain files: `if name.endswith(".md"):` — NEW S31
- `os.path.join(folder, name)` — glues a folder + filename into a full path using the OS's correct separator (`/` on Mac, `\` on Windows) — portable, and avoids double `//`. `os.path.join("puzzles", "greet.py")` → `'puzzles/greet.py'` — NEW S31

### Dictionaries
- Creating a dictionary: `person = {"name": "Dustin", "age": 30}`
- Accessing a value: `person["name"]` → `"Dustin"`
- Adding a key: `person["job"] = "developer"` — creates the key if it doesn't exist
- Updating a key: `person["age"] = 99` — overwrites the existing value
- `KeyError` — raised when you access a key that doesn't exist
- `len(dict)` — returns the number of key-value pairs
- `dict.keys()` — returns all keys in the dictionary
- `key in dict` / `key not in dict` — checks if a key exists: `"food" not in totals` → `True` if "food" hasn't been added yet

### List of Dictionaries
- A list can hold dicts as items: `items = [{"name": "eggs", "done": False}, {"name": "milk", "done": True}]`
- Access a field: `items[0]["name"]` → `"eggs"`
- Loop over and pull fields: `for item in items: print(item["name"], item["done"])`
- `.pop(index)` removes and returns the item at that position — the list holds dicts, so you get a dict back
- `str.split(",")` — splits a string on a delimiter, returns a list: `"eggs,False".split(",")` → `["eggs", "False"]`
- ⚠️ **bare `.split()` vs `.split(" ")`:** bare `.split()` (no argument) is "smart" — it treats any run of whitespace as one divider and trims the ends, so no empty strings (`"  a   b  ".split()` → `["a", "b"]`). Passing an explicit delimiter like `.split(" ")` is literal — it splits on every single space and does NOT collapse runs, producing empty strings `''` in the gaps. For word counting, always use bare `.split()`
- Reconstruct bool from file string: `parts[1] == "True"` — compares strings, result is a real boolean

### Accumulator Pattern
- Start a variable at `0` before the loop: `total = 0`
- Add to it each iteration: `total = total + item["field"]`
- After the loop, `total` holds the sum of all values

### Grouping and Accumulating
- Use a dict to hold a running total per category: `totals = {"Food": 0, "Transport": 0}`
- Inside the loop, use the category value as a key: `totals[e["category"]] = totals[e["category"]] + e["amount"]`
- `e["category"]` returns a string — that string is used as the key to look up in `totals`
- Loop over the dict to print results: `for key in totals.keys(): print(f"{key}: ${totals[key]:.2f}")`

### String Methods
- `str.capitalize()` — returns the string with the first letter uppercased, rest lowercased: `"burger".capitalize()` → `"Burger"`

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

### Scripting — command-line arguments (`sys.argv`) — NEW S30
- A **script** is code saved in a `.py` file and run from the terminal with `python3 file.py` (not typed line-by-line in the REPL)
- ⚠️ **REPL vs script:** the REPL auto-echoes the value of any bare expression you type; a script does NOT. A script only puts something on screen if you explicitly `print()` it. A bare `sys.argv` line in a file produces no output
- `import sys` then `sys.argv` — a **list** of the command-line pieces, built fresh every run
- **`sys.argv[0]` is always the script name** (e.g. `'argv_drill.py'`) — the list is never empty, even with no arguments
- Each word typed after the filename becomes its own list item, **split on spaces**: `python3 s.py hello world` → `['s.py', 'hello', 'world']`
- **Quotes group words into one argument:** `python3 s.py "hello world"` → `['s.py', 'hello world']`. Quote args that contain spaces or shell-special characters like `#` (e.g. `"#Nuggets"`)
- The first real argument you pass is `sys.argv[1]` (index 1, since 0 is the script name)
- Each run starts from a blank slate — `sys.argv` reflects only the command just typed; nothing persists between runs unless saved to a file
- Run a script that lives in a subfolder by its path: `python3 projects/argv_drill.py`

### Classes & Objects — writing your own (OOP) — IN PROGRESS, needs more reps
- A **class** is a blueprint; calling it with `()` builds an **object/instance**. `class Dog:` defines the blueprint
- A **method** is a function defined inside the class. Its first parameter is always **`self`** — but you don't pass it; Python auto-passes the object you called it on (`d.bark()` → `self` is `d`)
- **`self` = "this particular object."** Proven: `d.who_am_i() == d` is `True` — self is the instance, NOT the class
- **`__init__(self, ...)`** runs *automatically* when you create the object (`Dog("Rex")` triggers it). You never call it yourself
- **`self.name = name`** inside `__init__` stores incoming data as an **attribute** ON the object, so it persists. Without it, the value vanishes when `__init__` ends
- ⚠️ **Inside any method, the object's own data is ALWAYS `self.something`** — to *set* it (`self.desc = desc` in `__init__`) and to *read* it (`self.desc` in other methods). Using a bare name or a global variable instead is the classic bug
- Two moments: (1) object born → `__init__` runs, `self` = the new object; (2) method called later → `self` = the object you called it on
- Each object holds its **own** attributes — `d.name="Rex"` and `d2.name="Luna"` don't interfere. One blueprint, many objects, each with its own data (in memory; not saved to disk unless you write it to a file)
- ⚠️ **Method vs parameter:** a method is its OWN `def` line at the same indent as `__init__` (an ability). A parameter goes in the parens of a `def` line (data passed in). Don't cram a method name into `__init__`'s parens
- A method can take extra parameters beyond `self`: `def deposit(self, amount):` — call it `b.deposit(50)`, the `50` lands in `amount`. `self` is auto-passed, `amount` you pass
- **Give a method its data, don't let it fetch it:** prefer `deposit(self, amount)` over calling `input()` inside the method — a parameterized method works from a loop, a file, or a test, not only a human typing
- A class can store a **list as an attribute**: `self.songs = []` in `__init__` (fresh starting state, not a parameter); methods append via parameter (`add_song(self, title)` → `self.songs.append(title)`)
- Two kinds of `__init__` setup: data that varies per object (parameter → `self.name = name`) vs data that's always the same starting state (created fresh inside → `self.songs = []`)
- `self` is just the first parameter's NAME (could be anything); convention is always `self`. It is the **instance**, never the class
- CapWords convention for class names: `BankAccount`, not `bankaccount`
