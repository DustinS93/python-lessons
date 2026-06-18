# ROADMAP.md — CLI Expense Tracker

## The Project
A command-line expense tracker. The user can log expenses with a description, category, and amount. They can view all expenses, see totals by category, and quit — with expenses saved to a file so they persist between runs.

**Project file:** `projects/expense_tracker.py`

---

## How to Read This

Each step is either a **Learn** step or a **Build** step.

- **Learn** steps have two checkboxes: drilled in REPL and puzzle completed.
  Both must be checked before moving to the next step.
- **Build** steps are milestones where you write a working version of the
  project using what you've learned. The app should run after every build step.
- Check off boxes as you go. At session start, scan for the first unchecked box — that's where we are.

---

## Steps

### 1. `float` — decimal numbers for money
*Needed for: storing amounts like 4.99 instead of just 4*
- [x] Drilled in REPL
- [x] Puzzle

### 2. f-strings — clean string formatting
*Needed for: displaying amounts like `Food: $34.50` cleanly*
- [ ] Drilled in REPL
- [ ] Puzzle

### 3. List of dicts — storing structured data (extra drilling)
*Needed for: each expense is `{"desc": "coffee", "category": "Food", "amount": 4.99}`*
*Note: covered in session 16, but needs more reps before building on it*
- [ ] Drilled in REPL (revisit — extra session)
- [ ] Puzzle

### 4. Summing values from a list of dicts
*Needed for: calculating totals per category*
- [ ] Drilled in REPL
- [ ] Puzzle

### 5. Grouping and accumulating — looping to build category totals
*Needed for: "Food: $34.50, Transport: $12.00" from a flat list of expenses*
- [ ] Drilled in REPL (extra drilling — this is the core new pattern)
- [ ] Drilled in REPL (second pass)
- [ ] Puzzle

---

### BUILD v0.1 — Working core (no file saving yet)
*Prerequisites: steps 1–5 complete*
- [ ] App runs and shows a menu: `[1] Add Expense  [2] View All  [3] View Totals  [4] Quit`
- [ ] User can add an expense — description, category, amount stored as a dict in a list
- [ ] User can view all expenses — numbered, with category and amount
- [ ] View Totals shows a total per category
- [ ] Quit exits cleanly
- [ ] Menu loops with `while True`, `break` on quit

---

### 6. Saving and loading a list of dicts to/from a file
*Needed for: persisting expenses between runs*
*Note: file I/O was covered in session 15 but this is more complex — dicts with three fields*
- [ ] Drilled in REPL (extra drilling — focus here)
- [ ] Drilled in REPL (second pass)
- [ ] Puzzle

---

### BUILD v0.2 — Complete project
*Prerequisites: step 6 complete*
- [ ] On startup, load existing expenses from `expenses.txt` if it exists
- [ ] On quit, save current expenses to `expenses.txt`
- [ ] App is fully functional: add, view all, view totals, persist across runs
- [ ] Error handling on amount input (`try/except ValueError`)
- [ ] Committed to GitHub

---

## Stretch (after v0.2)
- [ ] Delete an expense by number
- [ ] Filter view by category
- [ ] Sort expenses by amount
