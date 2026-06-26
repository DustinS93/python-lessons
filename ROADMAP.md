# ROADMAP.md — GUI Expense Tracker (CustomTkinter)

## The Project
Rebuild the Expense Tracker as a **modern desktop app** with a real window —
entry boxes, buttons, and a scrolling list — instead of a text menu in the
terminal. Same logic you already know (add, view, totals, save/load to file);
the new skill is the **graphical user interface (GUI)** layer on top.

**Library:** CustomTkinter — a modern-looking skin over Python's built-in
Tkinter. The look is the skin; the concepts underneath are standard Tkinter and
transfer to any GUI toolkit.

**Project file:** `projects/expense_gui.py`

---

## The Big New Idea: Event-Driven Programming
Your CLI programs run top-to-bottom and stop. A GUI program **starts up, then
sits idle and waits.** It only runs code when the user *does something* — clicks
a button, types in a box. The function that runs in response is a **callback**.
Almost every new concept below is a piece of this one shift.

---

## How to Read This
Same as before:
- **Learn** steps have two checkboxes: tried in REPL/snippet and puzzle completed.
  Both must be checked before moving on.
- **Build** steps are milestones — the app should run after each one.
- At session start, scan for the first unchecked box — that's where we are.

**Note on drills for GUI:** A window needs an event loop, so we can't always do
one-line-at-a-time REPL drills. For visual concepts the drill becomes: *run this
small snippet and predict what appears on screen before you look.*

---

## Steps

### 1. Installing a third-party library + your first window
*Needed for: getting CustomTkinter onto your machine, and opening a window at all*
*Teaches: `pip install`, `import customtkinter`, the window object, `mainloop()`*
- [x] Tried in REPL/snippet (install it, open a blank window)
- [x] Puzzle — `my_first_window.py` (a titled, sized window that opens and waits)

### 2. Widgets — labels and buttons
*Needed for: putting things in the window*
*Teaches: `CTkLabel`, `CTkButton`, parent windows*
- [ ] Tried in REPL/snippet
- [ ] Puzzle — `hello_button.py` (a window with a label and a button in it)

### 3. Layout — positioning widgets
*Needed for: arranging the form neatly instead of stacked in one column*
*Teaches: geometry managers — `.pack()` and `.grid()`*
- [ ] Tried in REPL/snippet
- [ ] Puzzle — `layout_practice.py` (arrange 3 widgets deliberately)

### 4. Callbacks — making a button DO something
*Needed for: the whole app — every button runs a function. THE core concept.*
*Teaches: `command=` wiring a button to a function, event-driven flow*
- [ ] Tried in REPL/snippet
- [ ] Puzzle — `click_counter.py` (button click increments a number on a label)

### 5. Entry widget — reading what the user typed
*Needed for: capturing the description, category, and amount*
*Teaches: `CTkEntry`, `.get()` to read its text*
- [ ] Tried in REPL/snippet
- [ ] Puzzle — `greeter_gui.py` (type a name, click, label greets you by name)

### 6. Updating the display dynamically
*Needed for: showing new expenses and totals without restarting*
*Teaches: `.configure(text=...)` to change a widget, building output strings*
- [ ] Tried in REPL/snippet
- [ ] Puzzle — `add_to_list_gui.py` (type an item, click Add, it appears in a list)

---

### BUILD v0.1 — The Add form (in memory)
*Prerequisites: steps 1–6 complete*
- [ ] Window opens with three entry boxes: description, category, amount
- [ ] An "Add Expense" button stores the entry as a dict in a list
- [ ] A label confirms the add (e.g. "Added: coffee — Food — $4.99")
- [ ] App runs as a real window

---

### BUILD v0.2 — Showing the data
*Prerequisites: v0.1 complete*
- [ ] All expenses display in the window (a scrollable area or textbox)
- [ ] A "View Totals" area shows total per category
- [ ] Display refreshes after each add

---

### BUILD v0.3 — Persistence + safety (complete project)
*Prerequisites: v0.2 complete. Reuses your existing file logic.*
- [ ] On startup, load existing expenses from `expenses.txt` if it exists
- [ ] Save to `expenses.txt` after each add
- [ ] Error handling on amount input — bad input shows a message, doesn't crash
- [ ] Committed to GitHub

---

## Stretch (after v0.3)
- [ ] Delete an expense by selecting it in the list
- [ ] Filter the view by category (carried over from the CLI version)
- [ ] Sort expenses by amount (carried over from the CLI version)
- [ ] **Distribution** — package the app with PyInstaller into something a
      non-technical person can run without Python or a terminal (your stated goal)
