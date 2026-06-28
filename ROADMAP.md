# ROADMAP.md — Flask Walkthrough (a taste of web apps)

## The Point
A short, focused look at **how a web app actually works** — so Dustin can see
the machinery, not just use it. This is a *walkthrough*, not a big project. When
it's done we steer back to **getting good at core Python** (next frontier:
writing your own classes / OOP).

**Why Flask (not Django):** Flask is small — you see the *entire* request →
function → response cycle in one short file, nothing hidden. Django hides the
machinery, which is the opposite of what we want here.

**Project file:** `projects/flask_app/` (Flask wants a folder, not one file)

---

## The Big Idea (connects to what you know)
A GUI button click runs a **callback**. A web app is the same shape, just over
the internet:

> Browser asks for a URL → **your Python function runs** → it hands back a page →
> the browser shows it.

The function tied to a URL is called a **route handler** (Flask calls it a
**view function**). Same mental model as `command=on_click`, new venue.

**No JavaScript needed.** Python (logic) + HTML (structure) + CSS (style) build a
complete, real web app. Forms submit and the page reloads — that's legitimate
server-side rendering. JS is optional polish for *later, by choice*.

---

## How to Read This
Same format as always:
- **Learn** steps: tried in snippet + puzzle completed. Both before moving on.
- **Build** step is the milestone — the app should run in a browser after it.
- Drills here = "run this and predict what shows up in the browser."

---

## Steps

### 1. Install Flask + your first route
*Needed for: running a web server at all, seeing URL → function → response*
*Teaches: `pip install flask`, `Flask(__name__)`, `@app.route("/")`, `app.run()`, the dev server + localhost in the browser*
- [x] Tried in snippet (run the server, visit the URL, see text)
- [x] Puzzle — `hello_flask.py` (one route returns a line of text in the browser)

### 2. Returning HTML
*Needed for: a real page, not just plain text*
*Teaches: a view function can return an HTML string; the browser renders the tags*
- [ ] Tried in snippet
- [ ] Puzzle — add a second route that returns a small HTML page (heading + paragraph)

### 3. Templates — HTML in its own file
*Needed for: keeping HTML out of your Python; the proper way*
*Teaches: `render_template`, the `templates/` folder, passing a variable into a page with `{{ }}`*
- [ ] Tried in snippet
- [ ] Puzzle — `templates/page.html` rendered by a route, with one Python value injected

### 4. Forms — reading what the user typed (the web `.get()`)
*Needed for: input — the web version of `CTkEntry` + `.get()`*
*Teaches: an HTML `<form>`, GET vs POST, reading submitted data with `request.form`*
- [ ] Tried in snippet
- [ ] Puzzle — a form where you type a name, submit, and the next page greets you (web version of `greeter_gui.py`)

---

### BUILD — Tiny greeter web app
*Prerequisites: steps 1–4*
- [ ] A page with a form: type your name
- [ ] Submitting runs your Python and shows a page that greets you by name
- [ ] Runs in the browser at localhost
- [ ] Committed to GitHub

---

## After this walkthrough
Back to **core Python depth** — first target: **writing your own classes (OOP)**,
the natural next jump (you just hit classes via tkinter/Flask objects). Then
comprehensions and cleaner idioms. Reassess web vs. desktop once OOP is solid.

## Parked
- GUI Expense Tracker (CustomTkinter) — paused at Step 5 of 6, see
  `roadmaps/ROADMAP_expense_gui_PAUSED.md`. Taught the event-loop model; resume
  anytime if desktop becomes the goal again.
