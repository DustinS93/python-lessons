# VOCABULARY.md

All terms introduced so far. Update immediately when new vocabulary comes up —
consult mid-session when confirming a method or term.

| Term | Definition |
|---|---|
| parameter | The placeholder name in a function definition — `def greet(name)`, `name` is the parameter |
| argument | The actual value you pass when calling a function — `greet("Dustin")`, `"Dustin"` is the argument |
| default parameter | A parameter with a fallback value — `def greet(name, animal="dog")`. Must come after non-default parameters |
| keyword argument | Passing an argument by name when calling a function — `greet(greeting="Hi", name="Dustin")`. Order doesn't matter when you use the name |
| return value | The value a function hands back to the caller via `return`. Distinct from printing |
| truncation | Cutting off the decimal without rounding — `int(7.9)` gives `7`, not `8` |
| REPL | Read, Evaluate, Print, Loop — the interactive Python shell (`python3` in terminal) |
| script | Code saved in a `.py` file and run as a whole from the terminal (`python3 file.py`), not typed line-by-line in the REPL |
| command-line argument | A word typed after the script name when running it — `python3 greet.py Dustin`, `Dustin` is the argument. Python collects them in `sys.argv` |
| `sys.argv` | A built-in list of the command-line pieces. `sys.argv[0]` is always the script name; `sys.argv[1]` is the first real argument. Built fresh each run |
| shell / terminal | Where you launch scripts (prompt ends in `%` or `$`) — distinct from the REPL (`>>>`). `sys.argv` only fills when you launch a script here |
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
| attribute | A piece of data attached to an object — `self.desc`. Set in `__init__`, read anywhere via `self.` |
| `__init__` | The initializer/constructor method — runs *automatically* when you create an object. Sets up its attributes |
| `self` | Inside a class, "this particular object." Auto-passed when you call a method; the object being built inside `__init__` |
| instantiate | To create an object from a class — `Expense("Coffee", "Food", 3.33)` instantiates an Expense |
| immutable | Cannot be changed after it's created. Strings are immutable — `.upper()` can't edit `"python"`, it returns a NEW string instead |
| mutable | Can be changed in place after creation — lists are mutable (`.append()` modifies the original) |
| return value | The value a function/method hands back. `word.upper()` returns `'PYTHON'`; it's lost unless you assign it |
| `id()` | Built-in function giving an object's identity (roughly its memory address). Same `id` = the same object, not just an equal one |
| `is` vs `==` | `is` asks "same object?"; `==` asks "same value?". Compare strings with `==` — never `is` |
| garbage collection | Python reclaiming memory once nothing can reach an object. **garbage = unreachable** — there's no recycle bin and no way to get it back |
| interning | CPython storing one copy of short identifier-like strings and reusing it, so identical literals share an object. An optimization, not a language guarantee |
| method vs function | `word.upper()` is a method (object before the dot); `len(word)` is a function (thing inside the parens). Same idea, different shape |
