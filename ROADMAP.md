# ROADMAP.md — Expense Tracker: from script to shippable app

## The Point
Take `projects/expense_tracker.py` — an app you already understand — and rebuild it
so it can be **handed to someone who has never installed Python**.

You already know what the app does. That's deliberate: none of the effort goes into
figuring out the feature list, so all of it goes into the one new idea, which is
**how a program is put together**.

### The one idea, stated once
A program has three layers, and they are not the same thing:

| Layer | What it is | Can it be swapped? |
|---|---|---|
| **1. Logic** | Add, delete, total, save, load. Data in → data out. | No — this is the app |
| **2. Interface** | How a human drives it: terminal, GUI, web page | **Yes — this is the point** |
| **3. Packaging** | Bundling Python + your code into something double-clickable | Separate skill, separate tool |

**A function that RETURNS data can have any interface put on it. A function that
PRINTS has already chosen one, forever.** (S39: `letter_tally` vs `print_report`.)

Layer 2 is only swappable if layer 1 exists as its own thing. In the current file it
mostly doesn't — so that's Phase 1.

---

## How to Read This
- **Learn** steps: REPL drill + a small puzzle in `puzzles/`. Both ticked before moving on.
- **Build** milestones: change `projects/expense_tracker.py` itself.
- ⚠️ **Every build milestone must END RUNNABLE.** `v1.1` does less than `v1.2` but it
  runs, and it gets committed and pushed. No session ends on a half-torn-apart file.
- Pace: thorough over speed. No advancing until it's solid.

---

## PHASE 1 — Pull the logic out (still a terminal app)
*The app looks identical from the outside when this phase is done. That's the test.*

### 1. A function that returns instead of prints
*Teaches: the S39 lesson at project scale; why `print_list()` reading a global is a bug*
- [ ] REPL/drill — a function that builds a list and returns it vs one that prints it;
      try to reuse each one
- [ ] **Build v1.1** — `category_totals(expenses)`: takes the list, **returns** the
      totals dict. Menu option 3 calls it and does the printing. Same output on screen.

### 2. Functions with several parameters
*Teaches: passing more than one argument; order matters; still no `input()` inside*
- [ ] REPL/drill — define a 3-parameter function, call it with arguments in the wrong
      order and read what you get
- [ ] **Build v1.2** — `add_expense(expenses, description, category, amount)` and
      `delete_expense(expenses, position)`. The menu collects the input; the functions
      never call `input()`.

### 3. Display is interface, not logic
*Teaches: the boundary — what belongs in the logic layer and what doesn't*
- [ ] **Build v1.3** — fix `print_list()`: give it a parameter instead of a global,
      and rename it for what it does. Decide (and be able to defend) which side of the
      line it lives on.

### 4. Guard the edges
*Teaches: the interface layer is where bad input gets caught, so the logic can trust its arguments*
- [ ] REPL/drill — `int("abc")`, `float("")`, and what a bare `except:` hides
- [ ] **Build v1.4** — a non-numeric menu choice currently crashes the app. Fix it at
      the interface layer.

### PHASE 1 CHECKPOINT
- [ ] Every function takes what it needs as parameters. **No function reads a global.**
- [ ] No `input()` or `print()` inside any logic function.
- [ ] The app behaves exactly as it did before. Commit as **v1.0 — logic layer**.

---

## PHASE 2 — Put a different interface on it
*Nothing in Phase 1's logic changes. If it does, Phase 1 wasn't finished.*

- [ ] Re-warm CustomTkinter — `puzzles/my_first_window.py`, `layout_practice.py`,
      `click_counter.py`, `greeter_gui.py` already exist; reread before starting
- [ ] Learn — reading a value out of an entry widget vs the widget itself
      (known weak spot from S26)
- [ ] **Build v2.1** — a window that lists the expenses, using Phase 1's functions
- [ ] **Build v2.2** — add an expense from the GUI
- [ ] **Build v2.3** — delete, and show category totals
- [ ] **v2.0** — the GUI app runs. `expense_tracker.py` (terminal) still runs too,
      unchanged, off the same logic. **That's the proof the split worked.**

---

## PHASE 3 — Hand it to someone
*The finish line: a person with no Python and no terminal double-clicks it and it works.*

- [ ] Learn — why `"expenses.txt"` is a **relative** path, and why that breaks the
      moment someone else runs the app from somewhere else
- [ ] **Build v3.1** — save data somewhere that works on any machine
- [ ] Learn — what a bundler actually does (it ships a copy of Python inside your app)
- [ ] **Build v3.2** — build it into a double-clickable app with PyInstaller
- [ ] **v3.0** — send it to someone and watch them run it

---

## Parked (set aside on purpose)
- Scripting / vault tools — `roadmaps/ROADMAP_scripting_PAUSED.md` (resume at Step 4)
- OOP / writing your own classes — `roadmaps/ROADMAP_oop_PAUSED.md`
  - Worth revisiting *after* Phase 1: a class is one answer to "where does this data live"
- Flask web walkthrough — `roadmaps/ROADMAP_flask_walkthrough.md`
  - The alternative Phase 2 interface, if the GUI stops being fun
