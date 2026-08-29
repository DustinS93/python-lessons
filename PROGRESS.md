## Session 33 — 2026-08-28

### What We Covered
- **Direction pivot:** Scripting track felt dry + killed daily practice (~2 mo gap). Parked it (`roadmaps/ROADMAP_scripting_PAUSED.md`, resume Step 4). New `ROADMAP.md` = **Basics Reboot**, puzzle format, gaps front-loaded
- **Ground-floor assessment** (12 Q predict-output/write): 8/12 clean — logic core intact, misses were rust not absence. Gaps: zero-based indexing (×2), string concat spacing, string methods, method-call syntax
- Step 1 — **zero-based indexing**: `[0]` first, `[-1]` last, `IndexError` past end, `range(3)`→`[0,1,2]`; string=characters vs list=items
- Step 2 — **slicing**: `[start:end]` end EXCLUDED, `end-start`=count, blank start/end, `[-2:]` last-N (brand new to him, not rust)
- Step 3 — **building strings**: `+` needs same type (`str()` to add a number), `TypeError` on str+int; f-strings auto-convert, cleaner
- **Git model taught:** commit (local snapshot in `.git`) vs push (to GitHub); `add`→`commit -m`→`push`; three zones; ran the full loop himself

### Puzzles Completed
- `first_last.py`, `slice_it.py`, `greeting.py`

### Vocabulary Introduced
- slicing, staging area / `.git`, remote / origin, `str()` (revisited), f-string (revisited)

### What He Struggled With
- Slicing end-exclusion (predicted `[0:3]`→`pyth`, is `pyt`) — corrected on running
- `str + int` TypeError (predicted concat) — key Step 3 lesson
- `git commit "msg"` without `-m` (old habit) — corrected

### What Felt Solid
- Indexing drill 8/8 incl. the two he failed in the assessment an hour before
- Worked out `[-2:]` (last 2) unprompted; reached for `str(age)` unprompted in greeting.py
- Clean explain-backs on all three concepts; ran full git loop solo

### Where to Start Next Session
- ROADMAP **Step 4 — string methods** (`.upper()`, `.lower()`, `.strip()`, `.replace()`, the `object.method()` pattern) → puzzle `shout.py`
- Then Step 5 (list methods `.append()`) closes the same `object.method()` shape
- Keep the daily puzzle rhythm — momentum is the goal
