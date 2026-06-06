# AUDIT.md — System Review & Learner Assessment
*Written after Session 6 — 2026-06-05*

---

## Part 1: System Audit

### What's Working Well
- **Struggle-first rule** — this is the most important rule in the system and it's being followed. Don't soften it.
- **Shell drills before new concepts** — effective. You're building familiarity before applying.
- **Vocabulary tracking** — underrated. Most beginners skip this and pay for it later.
- **Committing after every puzzle** — good habit being built early.
- **"Read the error first" rule** — being followed consistently.

---

### Problems & Recommendations

#### 1. No curriculum roadmap
**Problem:** Sessions pick the next topic based on what "feels right." There's no map of where this is going or what the destination is.

**Fix:** Create a `ROADMAP.md` with an ordered list of concepts from now to a first real project. Having a destination makes the learning feel purposeful and makes it obvious when a concept is skipped or rushed. Suggested milestone: *build a CLI task manager* — it uses everything covered so far plus a few new concepts (file I/O, while loops, dictionaries).

---

#### 2. PROGRESS_LOG.md is out of chronological order
**Problem:** Sessions are logged in this order: 3, 2, 1, 4, 5, 6. Makes the log hard to read as a history.

**Fix:** Always append to the bottom. Consider adding a rule to CLAUDE.md: *new sessions go at the bottom of PROGRESS_LOG.md*.

---

#### 3. Shell drills aren't recorded
**Problem:** CLAUDE.md says "before using a method in a puzzle, confirm it was drilled first" — but there's no drill log. This rule is unenforceable and creates ambiguity.

**Fix:** Either drop the rule, or add a `DRILLS.md` that logs each drill by concept and date. A lightweight format works — one line per concept, checkmark when drilled.

---

#### 4. Puzzle files have no stated intent
**Problem:** `the_shopping_list.py` is just code. In 3 months you won't remember what it was meant to teach.

**Fix:** Add a one-line comment at the top of every puzzle file stating the concept it demonstrates. Example:
```python
# Concept: loop counter pattern — incrementing a variable inside a for loop
```
This is the one case where a comment is actually useful.

---

#### 5. No spaced repetition
**Problem:** Concepts are marked "solid" and never deliberately revisited. Memory doesn't work that way — solid today doesn't mean solid in two weeks.

**Fix:** Start each session with one REPL drill on a concept from 2+ sessions ago. Takes 2 minutes, dramatically improves retention. Add this to the Session Start section in CLAUDE.md.

---

#### 6. No mechanism for you to articulate what you learned
**Problem:** The progress notes are written by the AI. You're not required to explain anything back in your own words before moving on.

**Fix:** Before ending a session, add a step: "Explain back to me in one sentence what today's key concept was." If you can't explain it plainly, the session isn't done. This catches shallow understanding that drills and puzzles can miss.

---

#### 7. Dead code in puzzle files
**Problem:** `the_shopping_list.py` has `# number = number + 1` left in as a commented-out line. Small thing, but it's noise.

**Fix:** Before committing, clean up commented-out code. Add to Git Habits in METHOD.md: *delete commented-out code before committing*.

---

#### 8. METHOD.md has the wrong folder name
**Problem:** `METHOD.md` says the folder structure is `python-learning/` — the actual folder is `python-lessons/`.

**Fix:** Minor, but update it so the docs are accurate.

---

#### 9. No project milestone
**Problem:** Isolated puzzles are great for learning mechanics, but at some point they stop feeling meaningful. There's no larger goal to work toward.

**Fix:** Define a first project — something small but real. Suggestion: a **CLI shopping list manager** (add items, view list, mark done, save to a file). It touches: lists, loops, functions, input(), file I/O, and conditionals — everything you've built so far plus a natural next step.

---

## Part 2: Learner Assessment

### Where You Are
Six sessions in. You've covered: `print` vs `return`, parameters/arguments, default parameters, type conversion, conditionals, `input()`, scope, lists, and basic loops. That's a solid foundation — most of what Python needs to be useful.

### Genuine Strengths

**You read error messages.** This sounds basic but most beginners skip it and ask for help immediately. You consistently read the error, form a hypothesis, and try before asking. That's the most important debugging habit there is.

**You ask "why," not just "how."** The parameter naming question today — "could `fruit` be any word?" — is a conceptual question, not a mechanical one. That's the difference between someone who's memorizing patterns and someone who's building a mental model. You're doing the latter.

**You self-correct.** The `number = +1` mistake — you caught that yourself. The `return` inside the loop — you reasoned through it once reminded of what `return` does. You're not waiting to be told the answer.

**You make unprompted leaps.** `int(float("7.5"))` in session 2. Recognizing the redundant `>= 13` check in session 4. These weren't prompted — you reasoned to them. That's real understanding.

---

### Things to Watch

**Hardcoding values that should be dynamic.** The `number = 3` in the countdown puzzle. This is an extremely common beginner pattern and it *will* keep showing up. Every time you write a specific number, ask: "what if the input changes?" If the answer matters, use `len()` or a variable.

**`return` inside loops.** Tripped you up this session. The mental model to build: `return` exits the entire function immediately, not just the current iteration. You'll encounter this again — loops inside functions are everywhere.

**Cleaning up before committing.** Commented-out code in `the_shopping_list.py` made it into a commit. Get in the habit of a quick scan before every commit.

---

### Honest Assessment

You're moving faster than average. Six sessions covering this much ground, and the understanding is genuine — not just pattern matching. The "struggle first" approach is working exactly as intended: you're reasoning through problems rather than copying solutions.

The next phase — list methods, while loops, dictionaries, file I/O — will feel harder because the problems get more compositional. You'll need to combine more things at once. The habits you've built (read the error, try first, ask why) are exactly what will carry you through that.

The system is good. The gaps above are refinements, not overhauls.
