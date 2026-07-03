# REFERENCE.md — Ingrained Concepts & Parked Library Notes

Not read at session start. Consult mid-session if needed.

## Ingrained Concepts
Covered and solid — one-line summaries only.

- **Functions:** def, parameters, arguments, default params, return, print vs return, functions calling functions, passing return values as arguments
- **Type conversion:** str(), int(), float(), int(float()), int(input())
- **Input:** input("prompt") — always returns a string
- **Conditionals:** if/elif/else — top to bottom, stops at first true condition
- **Scope:** local (inside function) vs global (outside). Same name in both scopes = local copy used inside the function
- **Lists:** create, index [0]/[-1], len(), for item in list, .append(), .remove(), .pop() (no args — removes last), item in list, list[i] = value
- **Loops:** for loop counter pattern, while condition, while True/break, break vs return vs continue
- **Storing return values:** result = function()

---

## Parked: GUI — CustomTkinter
*Project parked S27 (pure-Python direction, no libraries). Reference only — reload into Active Concepts if GUI resumes.*

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

---

## Parked: Flask (explored as a walkthrough — reference only, NOT a drilled/tracked concept)
*Dustin did this as a "see how it all fits together" tour (session 27), not to learn as a skill. Kept here as a reference if he returns to web; it does not count as active learning and won't be drilled.*

- `from flask import Flask` — import the Flask class
- `app = Flask(__name__)` — build the app object (`__name__` = boilerplate telling Flask the current file)
- `@app.route("/")` — a **decorator** mapping a URL path to the function below it. `"/"` is the homepage
- The function under the route is the **view function** — runs on request; whatever it **returns** is what the browser shows (return a string → browser shows that text)
- `app.run(debug=True)` — starts the dev server (the web's event loop, like `mainloop()`); `debug=True` auto-reloads on edit + shows errors in the browser
- Run with `python3 hello_flask.py`, then open the printed `http://127.0.0.1:5000` in the browser. Stop the server with **Ctrl+C**
- Mental model: URL request → view function runs → return value rendered. Same shape as button click → callback
- You can have **many routes**, each its own path + its own uniquely-named view function (`/` → `home()`, `/other` → `other()`). Visit a path at `http://127.0.0.1:5000/other`
- A view function can return a string of **HTML tags** (`"<h1>..</h1><p>..</p>"`) — Python *builds* the HTML text on the server and sends it; the browser renders it. Python never runs in the browser
- The browser only understands HTML (structure) / CSS (style) / JavaScript (in-browser logic). Python runs on the **server** and produces HTML — that's why no JS is needed for a working app
- **Templates:** import `render_template` (name only — `from flask import Flask, render_template`); a view function returns `render_template("page.html")`. HTML files live in a `templates/` folder; you pass just the filename, Flask looks in `templates/` automatically
- **Injecting Python values:** `render_template("page.html", name="Dustin")` passes a keyword argument; in the HTML use `{{ name }}` (Jinja2 placeholder — like an f-string's `{}` but inside HTML). The word in `{{ }}` must match the keyword passed
- **Project structure:** `app.py` (logic/routes) · `templates/` (HTML files) · `static/` (CSS, JS, images — served as-is). The `.py` renders the HTML; the HTML links the CSS
- **Linking CSS:** in the HTML `<head>`: `<link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">`. You do NOT import CSS in Python — the HTML links it and the browser fetches it
- ⚠️ HTML attributes are separated by **spaces, not commas** (`rel="stylesheet" href="..."`). Python habit of comma-separating breaks the tag
- ⚠️ A CSS class selector (`.sent_style`) must match the HTML `class="..."` **exactly**, letter for letter — a typo means the style silently never applies (no error, just no effect)
