## Session 39 — 2026-09-04

### What We Covered
- **Opener (parked S38 concept): the slice step slot** `[start:end:step]` — cold, with the position diagram. `[0:6:2]` → `'rbo'`, `[::2]`, then negative step
- A **negative step walks positions backwards**; blank slots flip (blank start = the end). `[::-1]` is not a "reverse switch" — reversal is the *consequence*
- ⚠️ **`end` is excluded whichever way you walk** — `"reboot"[5:0:-1]` → `'toobe'`, `r` missing. He derived the empty-string trap `[0:6:-1]` unaided
- **Slicing is forgiving, indexing is not** — out-of-range end is fine; `word[99]` is an `IndexError`
- A slice is an **expression, not a loop** — one new string in one go, vs S38's accumulator loop
- **CAPSTONE `word_stats.py`** — `letter_tally(word)` returns a dict; report prints outside it
- **Single responsibility** — one function, one job; the tell is needing the word "and" to describe it
- A **function calling another function**: `print_report` calls `letter_tally` itself and stores the result

### Puzzles Completed
- `puzzles/word_stats.py` (CAPSTONE — Basics Reboot complete)

### Vocabulary Introduced
- step (slice slot), single responsibility

### What He Struggled With
- ⚠️ **Repeated S38's silent-global bug in his own code** — put `tally = {}` OUTSIDE the function, so call 2 inherited call 1's counts (`e: 3` for "hello"). Diagnosed it himself once shown; cause was **pattern-matching `tally.py`'s flat-script shape into a function** (the S31 habit)
- Said "before the loop, inside the function" *before* writing — then wrote it outside. Words right, code wrong
- Refactor put the whole report inside `letter_tally` → two jobs, and `result =` had nowhere to go
- Wrapped a `None`-returning function in `print()` → stray `None`s
- Words under load: `return` "exits the loop" (it exits the **function**); "-1 tells it to start at the last letter" (it's the **step**); "outdated" info (it's **left over**)
- Naming: `word_to_pass`/`word_to_pass2`; then proposed `escapade = "escapade"`

### What Felt Solid
- **`return` after the loop, cold and unprompted** — no pointer to `score_total.py` needed
- Accumulator dict + `if`/`else` written correctly from scratch — better than the saved `tally.py`
- Stored the return value instead of assuming the function printed; `for k, v in .items()` cold
- Fixed the global, the two-job split, and the `None` wrapper with questions only — no code given
- Flagged honestly that `[::-1]` was recall, not derivation — then derived the variations

### Where to Start Next Session
- `puzzles/tally.py` was saved broken (missing its `else`) — **he found and fixed it at the end of S39**, output now correct. Don't re-use as an opener
- **Next track DECIDED (end of S39): Expense Tracker — script to shippable app.** New `ROADMAP.md` written; Basics Reboot archived to `roadmaps/ROADMAP_basics_reboot.md`
- Start at **Phase 1, Step 1** — drill return-vs-print reuse, then Build v1.1: extract `category_totals(expenses)` (it's `letter_tally` with a different accumulator)
- Opener first: a concept from 2+ sessions ago. **`return` in a loop is at streak 1 of 2** — v1.1 is a natural second appearance, so do NOT hint the accumulator placement
