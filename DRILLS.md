# DRILLS.md — Active Concepts

This is the session-start read. The rest of the reference system lives in:
- `VOCABULARY.md` — all terms (update immediately when new vocab comes up)
- `PUZZLE_INDEX.md` — concept → puzzle file map (consult when Dustin is stuck; update after each puzzle)
- `REFERENCE.md` — ingrained concepts + parked library notes (GUI, Flask)

Verbose detail for concepts not yet fully ingrained. When a concept is fully
ingrained, move it to `REFERENCE.md` as a one-line summary.

---

### Indexing & Slicing — NEW S33
- **Zero-based**: positions start at `0`. `"python"[0]` → `'p'` (first), `"python"[5]` → `'n'` (last)
- `[-1]` = last item, `[-2]` = second-to-last. Works no matter the length
- Indexing past the end → **`IndexError`** (`"python"[6]` errors)
- Same rule for lists: `nums[0]` = first **item**, `nums[-1]` = last. (Strings hold *characters*, lists hold *items/elements*)
- **Slicing** `[start:end]` grabs a **range** — the `end` is **excluded** ("up to, but not including"). `"python"[0:3]` → `'pyt'` (positions 0,1,2 — NOT 3)
- Trick: `end - start` = how many you get. `[0:3]` → 3 chars
- Blank start = from the beginning (`[:2]` → `'py'`); blank end = to the end (`[2:]` → `'thon'`); both blank = the whole thing (`[:]` → `'python'`)

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
- **The `object.method()` shape** — the object goes BEFORE the dot, not inside parens. Compare: `len(word)` is a plain **function** (thing goes inside); `word.upper()` is a **method** (thing goes before the dot) — NEW S34
- **Parens are required.** `word.upper` (no parens) does NOT error and does NOT run — it returns the method object itself (`<built-in method upper of str object ...>`). The `()` is what actually *calls* it — NEW S34
- `str.upper()` — returns a new string, all uppercase: `"python".upper()` → `'PYTHON'` — NEW S34
- `str.lower()` — returns a new string, all lowercase — NEW S34
- `str.replace(find, replace_with)` — returns a new string with every occurrence of the 1st argument swapped for the 2nd: `"a,b,c".replace(",", "-")` → `'a-b-c'`. Original unchanged — NEW S34
- ⚠️ **Strings are IMMUTABLE** — a string method can never change the original. It **returns a brand-new string** and leaves the old one untouched. Two questions every time: *what does it return*, and *did you keep it?* — NEW S34
- **Nothing is saved unless you assign it:** `word.upper()` alone evaporates; `word = word.upper()` catches the returned value. Right side runs first, result gets stored in the name on the left — NEW S34
- `.strip()` removes whitespace from **both ends only** — never from the middle. `"  a b  ".strip()` → `'a b'` (inner space kept)
- Methods **chain** — each returns a string, so the next method can act on it: `"  hi  ".strip().upper()` → `'HI'` — NEW S34

#### Names, objects, and identity (the model underneath) — NEW S34
- A variable is a **name pointing at an object**. Assignment re-points the name; it never edits the object
- `id(x)` — built-in function returning the object's identity (roughly its memory address). Same `id` = literally the same object
- `x is y` — asks "**same object?**". `x == y` — asks "**same value?**". ⚠️ **Always compare strings with `==`, never `is`**
- **garbage collection** — when nothing can reach an object any more, Python reclaims its memory. **garbage = unreachable**, so there is no way to retrieve it. Not a recycle bin; no undo
- **interning** — CPython optimization: short, identifier-shaped strings (letters/digits/underscore) are stored once and reused, so `"python" is "python"` → `True`, while `"hello world"` (has a space) typically → `False`. An implementation detail, NOT a language rule — never write code that depends on it
- Preview: **lists are MUTABLE** — `.append()` really does change the original in place. That contrast is the point of Step 5

### List Methods — changing a list in place — NEW S34
- Same `object.method()` shape as string methods — but lists are **MUTABLE**, so the rules invert
- `list.append(item)` — adds `item` to the **end** of the list, **changing the original in place**. No assignment needed
- `list.remove(value)` — removes the **first item equal to that VALUE** (not a position). `[1,2,3,4].remove(2)` → `[1,3,4]`
- ⚠️ **`.remove(value)` vs `.pop(index)`** — `.remove()` takes a **value**, `.pop()` takes a **position**. Easy to confuse; they take completely different arguments
- ⚠️ **In-place methods return `None`.** `nums.append(5)` returns nothing at all. Python convention: *a method that mutates the object returns `None`* — a deliberate warning that the work already happened to the original
- ⚠️ **THE TRAP:** `nums = nums.append(5)` is a **bug** — it overwrites `nums` with `None` and destroys the list. **No error is raised**; it fails much later when something tries to use `nums` as a list
- **The rule:** strings → `word = word.upper()` (must assign). Lists → `nums.append(5)` (never assign). Immutable = catch the new value; mutable = don't
- **The REPL hides `None`** — it echoes every value *except* `None`. A silent REPL does NOT mean there was no value. Use `print(x)` or `type(x)` to see it

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

### Searching inside text — `in` and `re` (regex) — NEW S32
- **`substring in text`** — a **boolean** test: `True` if `substring` appears anywhere inside the string. `"#Nuggets" in text`. **Case-sensitive** — `"nuggets"` ≠ `"Nuggets"`. Limit: you must already know the exact thing you're searching for; it can't *discover* or list all matches
- **regex (regular expression)** — a **pattern** describing a *shape* of text, not one exact string. Lets you find every substring of that shape, even ones you've never seen. Built-in module: `import re`
- **`re.findall(pattern, text)`** — returns a **list of every substring** matching `pattern`, in order, **including duplicates** (does NOT dedupe). No matches → empty list `[]`
- **raw string `r"..."`** — prefix that tells Python NOT to interpret backslashes (so regex codes like `\w` reach the regex engine intact). Regex patterns always go in `r"..."`
- Pattern pieces so far:
  - `#` — a **literal** character (matches an actual `#`)
  - `\w` — one **word character**: any letter, digit, or underscore
  - `+` — **one or more** of the thing right before it
  - `\w+` grabs a **run** of word characters and **stops at the first non-word char** (space, `-`, `.`, etc.)
- Tag pattern: **`re.findall(r"#\w+", text)`** → `['#Nuggets', '#Coffee']`. `#\w+` = "a `#`, then one or more word characters." A `#` with no word char after it (e.g. `"# b"`) → no match at all (the `+` needs at least one)
- More pattern pieces (for `[[links]]`):
  - `\[` / `\]` — **escaped** literal brackets. `[` and `]` are special in regex, so a backslash means "match an actual bracket." Obsidian links = `\[\[` ... `\]\]`
  - `.` — matches **any single character** (letter, space, digit, punctuation)
  - `.+` — one or more of any character (a run of "whatever's in the middle")
  - **greedy vs lazy:** plain `.+` is **greedy** — grabs as MUCH as possible, so `\[\[.+\]\]` swallows two links + the text between them as one match. Add `?` → **`.+?`** is **lazy** (non-greedy) — grabs as FEW as possible, stopping at the first `]]`, giving each link separately
  - **capture group `( )`** — marks "the part I want." When a pattern has a group, `re.findall` returns **only what's inside the parens**, dropping the rest of the match (the brackets still have to match, but aren't returned)
- Link pattern: **`re.findall(r"\[\[(.+?)\]\]", notes)`** → `['Daily Note', 'Project Ideas']` (names only, brackets stripped by the capture group + lazy match)

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
