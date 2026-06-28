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
| library / package | Pre-written code you import and use. `tkinter` is a *standard library* (ships with Python); `customtkinter` is a *third-party package* (must be installed) |
| pip | Python's package installer — downloads packages from PyPI and installs them. `python3 -m pip install <name>` installs into *that* Python |
| dependency | A package your package needs to work — pip installs them automatically (e.g. customtkinter pulled in `darkdetect` and `packaging`) |
| GUI | Graphical User Interface — a window with buttons/boxes, vs a text-only CLI (command-line interface) |
| event-driven programming | Program starts, then sits idle and *reacts* to user actions, instead of running top-to-bottom and stopping |
| event loop / `mainloop()` | The endless loop `mainloop()` starts: watch for events (clicks, keypresses) and run matching code. Program stays "busy waiting" until the window closes |
| widget | A single building block of a GUI window — a label, button, entry box, etc. |
| callback | A function you hand to a widget (via `command=`) that runs *later*, when the user triggers it (e.g. clicks the button). You pass it by name, no parens |
| class | A blueprint/template that describes what something *is* and can *do* — e.g. `CTk`, `CTkEntry`, `Flask`. Not a thing yet; a cookie cutter, not a cookie |
| object / instance | The actual thing built from a class by calling it with `()` — `app = Flask(__name__)` builds one Flask object. `app` is the instance |
| method | A function that belongs to an object, called with a dot — `app.run()`, `entry.get()`, `label.configure()`. "Reach into this object and use one of its abilities" |
| argument (parent window) | The first argument to a widget, e.g. `CTkEntry(app)` — tells the widget which window it lives in (its parent) |
| Flask | A small third-party web framework. `Flask(__name__)` builds your app object |
| route | A URL path mapped to a Python function — `@app.route("/")` maps the homepage to a function |
| view function / route handler | The function that runs when its route is requested — the web's version of a callback. Whatever it returns is what the browser shows |
| decorator | A line starting with `@` placed on top of a function that registers/modifies it — `@app.route("/")` attaches the function below to a URL |
| localhost | `127.0.0.1` — your own machine. The Flask dev server runs here; `:5000` is the port |

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
| f-strings — formatting variables and floats inside strings | `receipt_printer.py` |
| list of dicts — accessing fields, passing to functions, `.capitalize()` | `menu_board.py` |
| accumulator pattern — summing a value across a list of dicts | `score_total.py` |
| grouping and accumulating — dict of totals, looping to print with `.keys()` | `category_totals.py` |
| saving and loading a list of dicts to/from a file — round-trip via comma-separated .txt | `movie_log.py`, `workout_log.py` |
| try/except ValueError + range validation — checking input falls within 1 to 10 | `input_validator.py` |
| GUI window + widgets — CustomTkinter CTk(), CTkLabel, CTkButton, .pack(), mainloop() | `my_first_window.py` |
| GUI layout — .grid(row, column), row=down/column=right, no pack/grid mixing | `layout_practice.py` |
| GUI callbacks — `command=` wiring a button to a function, `.configure(text=)`, `global` in a callback | `click_counter.py` |
| GUI input — `CTkEntry`, `.get()` to read typed text, update a label with an f-string | `greeter_gui.py` |
| Flask first route — `Flask(__name__)`, `@app.route("/")`, view function, `app.run()`, localhost in browser | `flask_app/hello_flask.py` |

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
- `key in dict` / `key not in dict` — checks if a key exists: `"food" not in totals` → `True` if "food" hasn't been added yet

### List of Dictionaries
- A list can hold dicts as items: `items = [{"name": "eggs", "done": False}, {"name": "milk", "done": True}]`
- Access a field: `items[0]["name"]` → `"eggs"`
- Loop over and pull fields: `for item in items: print(item["name"], item["done"])`
- `.pop(index)` removes and returns the item at that position — the list holds dicts, so you get a dict back
- `str.split(",")` — splits a string on a delimiter, returns a list: `"eggs,False".split(",")` → `["eggs", "False"]`
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

### GUI — CustomTkinter
- `import customtkinter` — the third-party GUI library (modern skin over Tkinter)
- `app = customtkinter.CTk()` — creates the main window object
- `app.title("...")` — sets the window's title bar text
- `app.geometry("400x300")` — sets the window size in pixels (width x height) as a string
- `app.mainloop()` — starts the event loop; window stays open and waits until closed
- The program does NOT end at the last line — `mainloop()` keeps it running until the window closes
- Widgets: `customtkinter.CTkLabel(parent, text="...")`, `customtkinter.CTkButton(parent, text="...")` — first argument is the PARENT window
- Naming convention: all widgets are `CTk` + widget name — `CTkLabel`, `CTkButton`, `CTkEntry`
- `widget.pack()` — places the widget into the window so it's visible. Creating a widget alone does NOT show it
- All widgets must be created BEFORE `mainloop()`, and `mainloop()` must be empty and the last line
- Discovering the API yourself: `dir(customtkinter)` lists what's available; `help(customtkinter.CTkButton)` shows its arguments (press `q` to exit)
- Layout (geometry managers): `.pack()` stacks widgets (top-down; options `pady`, `padx`, `side`); `.grid(row=, column=)` places in a table — `row` moves down, `column` moves right
- ⚠️ Never mix `.pack()` and `.grid()` in the same window/container — it freezes the program. Pick one per container
- Callbacks: `CTkButton(app, text="...", command=my_func)` — pass the function by **name, no parens**. Parens (`command=my_func()`) call it once immediately and hand the button the *result*, so the click does nothing
- The callback function must be **defined before** the button that references it
- `widget.configure(text="new text")` — changes a widget's property (e.g. its text) *after* creation. This is how a label updates on screen
- A global counter changed inside a callback needs `global count` as the first line of the function (same scope rule as `the_vault.py`) — otherwise `UnboundLocalError`
- ⚠️ When a callback crashes, the **window keeps running** (button looks dead) but the error prints to the **terminal** — always check the terminal when a click "does nothing"
- `entry = customtkinter.CTkEntry(app)` — a text input box. Show it with `.pack()`/`.grid()` like any widget
- `entry.get()` — returns the current text in the box, always **as a string** (like `input()` did). Call it inside a callback (read on click)
- Widgets are created **once** before `mainloop()`. A callback never *creates* widgets — it only **reads** them (`.get()`) and **updates** them (`.configure()`)
- Name the widget and the value differently — `name_entry` (the box) vs `typed = name_entry.get()` (the string). Reusing one name clobbers the widget and re-triggers the scope trap
- `print()` always goes to the **terminal**, never the window. To show text to the user, update a widget with `.configure(text=...)`

### Classes & Objects (just using them, not writing yet)
- A **class** is a blueprint (`CTk`, `CTkEntry`, `Flask`); calling it with `()` builds an **object/instance** (`app = Flask(__name__)`)
- A **method** is a function that belongs to an object, called with a dot: `app.run()`, `entry.get()`, `label.configure()`
- You've been *using* classes since the first GUI step — writing your own (OOP) is the planned next core-Python topic

### Flask (web apps)
- `from flask import Flask` — import the Flask class
- `app = Flask(__name__)` — build the app object (`__name__` = boilerplate telling Flask the current file)
- `@app.route("/")` — a **decorator** mapping a URL path to the function below it. `"/"` is the homepage
- The function under the route is the **view function** — runs on request; whatever it **returns** is what the browser shows (return a string → browser shows that text)
- `app.run(debug=True)` — starts the dev server (the web's event loop, like `mainloop()`); `debug=True` auto-reloads on edit + shows errors in the browser
- Run with `python3 hello_flask.py`, then open the printed `http://127.0.0.1:5000` in the browser. Stop the server with **Ctrl+C**
- Mental model: URL request → view function runs → return value rendered. Same shape as button click → callback

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
