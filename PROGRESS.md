## Session 28 — 2026-06-29

### What We Covered
- OOP reps from scratch, pure Python (spaced repetition of S27 — he asked to revisit)
- REPL drill: `Counter` class — `__init__`/`self`, a method that returns (`show`), then a mutating method (`add_one`/`sub_one`) reading+writing `self.count` inside the method
- Method-with-no-`return` displays nothing in REPL but still changes the object
- Distinguished parameter vs method (own `def` line); `start` is data you pass (`Counter(5)` → start=5), `self` is auto-passed
- `self` is just a parameter name (could be `thing`); convention = `self`; it's the INSTANCE, not the class
- Each class has its own `__init__`/`self`; multiple objects keep separate data (`c` vs `c2`)
- Design: method should take data via a parameter (`deposit(amount)`), not call `input()` itself
- Class naming convention: CapWords (`BankAccount`)

### Puzzles Completed
- `puzzles/bank_account.py` (BankAccount class from scratch: `__init__`, `deposit(amount)`, `withdraw(amount)`, `show()`)

### Vocabulary Introduced
- (none new — reinforced: self, instance, method vs parameter, attribute)

### What He Struggled With
- Method-vs-parameter twice: put `add_one` in `__init__` line; called `deposit(50)` before adding the `amount` param (TypeError — caught both himself via the error)
- Explain-back: first said `self` "refers to the class" — corrected to instance (had proven it earlier same session)

### What Felt Solid
- `self.attr` read+write INSIDE methods — clean all session (last session's core bug, now gone)
- Read every error and diagnosed it himself (TypeError "2 given", `__init__` missing arg)
- Sharp unprompted questions (can `self` be renamed? can two classes both have `__init__`?)
- Wrote a full BankAccount class COLD, predictions matched results

### Where to Start Next Session
- Stretch class: one that holds a LIST of things (he parked this himself), and/or a method that calls another method on the same object
- Watch: `self` = instance not class (slipped in explain-back) — re-confirm early
- Reinforce method-vs-parameter (his recurring trip-up this session)
- See ROADMAP.md (Core Python / OOP track)
