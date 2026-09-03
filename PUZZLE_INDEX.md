# PUZZLE_INDEX.md

Concept → puzzle file map. Consult when Dustin is stuck on a concept — point
him to the puzzle that covered it. Update after every completed puzzle.
Never repeat a concept already covered here.

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
| Flask templates — `render_template`, `templates/` + `static/` folders, linking CSS, `{{ }}` value injection (Jinja2) | `flask_app/` (templates/about.html + static/style.css) |
| Writing your own class — `class`, `__init__`, `self`, attributes, a method using `self` | `expense_class.py` |
| Class from scratch — `__init__` stores starting data, methods take an `amount` parameter and read+write `self.x`; method vs parameter | `bank_account.py` |
| Class holding a list — `self.attr = []` in `__init__`, method appends via parameter (no `input()` inside), for loop in `show` | `playlist.py` |
| Command-line arguments — `sys.argv`, running a script from the terminal, `argv[1]` as first arg, script vs REPL printing | `greet.py` |
| Read a file whose path comes from `sys.argv[1]` — `open(argv[1])`, `.read()` → one string, `.split()` + `len()` to count words | `wordcount.py` |
| Scan a folder — `os.listdir(folder)` → list of names, `for` loop + `if name.endswith(".md")` filter, folder path from `sys.argv[1]` | `list_notes.py` |
| Zero-based indexing — `[0]` first char/item, `[-1]` last, out-of-range `IndexError`, joining two indexes with `+` | `first_last.py` |
| Slicing — `[start:end]` grabs a range, end **excluded**; blank start/end; negative-start slice `[-2:]` for last N | `slice_it.py` |
| Building strings — `+` concatenation (same-type only, `str()` to add a number), vs f-strings (auto-convert, cleaner) | `greeting.py` |
| String methods — `object.method()` shape, `.strip()`/`.upper()`/`.replace()`, **immutability** (original never changes), method chaining + why chain order matters | `shout.py` |
| List methods — `.append()`, `.remove(value)` vs `.pop(index)`, lists are **mutable** (change in place), in-place methods return `None`, `len()` live vs snapshot, avoid shadowing built-ins | `todo.py` |
| Loops — `for` over a list, `range(n)` / `range(start, end)` (end excluded, same as slicing), looping by index with `range(len(x))`, `i` = position vs `x[i]` = item, shifting the display with `i + 1` (never the index) | `count_up.py` |
| Conditionals — `if`/`elif`/`else` chain, comparison operators, ordering tests most-restrictive-first, chain runs at most ONE branch, boundary testing (`>=` includes the number), placing a line inside a branch vs outside the chain, `return` vs `print` from a function | `grade.py` |
| Dicts deeper — accumulator dict (counting), `in` searches KEYS only, add-vs-update with the same syntax, `KeyError` vs `IndexError` (dicts have no positions), `.items()` + tuple unpacking (`for k, v in ...`), views vs snapshots, tuples are immutable | `tally.py` |
