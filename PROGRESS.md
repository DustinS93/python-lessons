## Session 27 — 2026-06-28

### What We Covered
- Flask walkthrough (install → routes → HTML → templates → static CSS → `{{ }}` injection) — done as a TOUR to see how the web fits together, NOT learned as a skill (his framing). Marked "explored, not learned" in DRILLS
- "What runs where" model: server vs browser; client-side JS can't be the source of truth, but Node runs JS server-side — so it's client-vs-server, not Python-vs-JS
- When you need a backend (Flask) vs static HTML/CSS/JS: stored data, secrets, accounts, data-driven pages
- **Pivot to pure Python — OOP:** writing your own class. `class`, `__init__`, `self`, attributes, a method using `self`
- Drills: `Dog` class — `self` is the instance not the class (`d.who_am_i() == d` → True); two objects each keep their own data

### Puzzles Completed
- `puzzles/expense_class.py` (first hand-written class: `Expense` with `__init__` + `summary()`)
- (Flask `flask_app/` built as a tour — reference only, not a tracked puzzle)

### Vocabulary Introduced
- class, object/instance, method, attribute, `__init__`, `self`, instantiate (+ Flask tour terms: route, view function, decorator, localhost — reference only)

### What He Struggled With
- Inside `summary()` used bare names / global `e` instead of `self.desc` (the core OOP bug — flagged it himself after)
- Added an unnecessary `for` loop inside `summary` (pattern-matched to old list-looping tracker; also a return-inside-loop echo)
- Got frustrated ("im way off") while actually one fix from done — spirals when close
- Flask tour debugging: called `render_template` on the import line, empty templates, HTML comma, CSS class typo

### What Felt Solid
- Class + `__init__` + storing attributes on `self` — correct first try (the hard part)
- Realized the rule himself: "self.desc should be used the whole time" — the key OOP insight
- Sharp conceptual questions (Node/server-vs-client, when-is-a-backend-needed)

### Where to Start Next Session
- OOP reps from scratch, PURE PYTHON, NO libraries — open with a small class drill, rebuild `__init__`/`self` while fresh (he asked to go over it a few more times)
- Watch: `self.attr` access inside methods (used global/bare name) — design next class to surface it
- When he says "I'm way off," point at what's RIGHT first — he's usually closer than he thinks
- See ROADMAP.md (new Core Python / OOP track). GUI + Flask both parked in roadmaps/
