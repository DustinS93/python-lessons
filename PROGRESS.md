## Session 34 — 2026-08-30

### What We Covered
- **Opener drill — dict access (cold):** wrote `f"{item} costs ${prices[item]}"` unprompted. **Fluency gap RESOLVED.** But called a key a "value" and said "the 2 indicie" — list thinking on a dict
- Step 4 — **string methods**: `object.method()` vs plain functions, parens required; `.upper()`, `.lower()`, `.strip()` (both ends only), `.replace(find, new)`. **Strings IMMUTABLE** — return a NEW string, nothing saved unless assigned. Found **chaining** himself
- **Deep detour he drove:** garbage collection (`garbage = unreachable`), `id()`, `is` vs `==`, **interning** (predicted `False`, got `True`)
- Step 5 — **list methods**: `.append()`, `.remove(value)` vs `.pop(index)`, `.pop()` returns the item. **Lists MUTABLE** — change in place, return `None`; the trap `nums = nums.append(5)` destroys the list with no error, ran it and broke his own
- `None` invisible in the REPL; **shadowing built-ins** (`list` → `tasks`); **snapshot vs live value** (stale `task_count` → `len()` inside the f-string)

### Puzzles Completed
- `shout.py`, `todo.py`

### Vocabulary Introduced
- immutable, mutable, return value, in place, `id()`, `is` vs `==`, garbage collection, interning, `None`/`NoneType`, shadowing, method vs function, chaining

### What He Struggled With
- Predicted `result = nums.append(5)` holds `5`; then thought `.append()` itself was "a bug" — needed method vs assignment split apart
- Term slips: `len()` returns a "str" (int); "key" called a "value"; dicts have "indicies". Miscounted `[1,2,3,4].remove(2)` → `[1,3]`
- Skipped the `word.upper` no-parens line four times — theorized past the drill

### What Felt Solid
- Chained methods unprompted; explained the chain-order/case-sensitivity bug cold
- Sharp unprompted questions (can you retrieve garbage; is a re-created literal the same object); diagnosed the stale-`task_count` bug himself
- Clean final explain-back on immutable vs mutable; ran the full git loop solo twice

### Where to Start Next Session
- ROADMAP **Step 6 — loops** (`for x in list`, `range(n)`, index) → `count_up.py`
- **Placement weak spot gets its first real appearance** — do NOT guide block structure
- Reinforce dict-vs-list model at Step 8 — the "indicies" slip showed it's soft
