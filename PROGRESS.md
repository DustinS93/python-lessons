## Session 32 — 2026-08-04

### What We Covered
- Warm-up (spaced rep, S30): REPL auto-echoes a **bare expression** (raw stored value, `\n` shown literally); a **script** does NOT — silent unless `print()`. Proved it live with `scratch.py`
- Defined **bare expression** (value-producing code typed alone); SyntaxError (bad grammar) vs NameError (valid name, doesn't exist) off his own typo
- Step 4 concept — searching inside text:
  - `substring in text` → boolean, case-sensitive; limit = must know exact text, can't discover
  - `re.findall(pattern, text)` → list of ALL matches (dupes included), `[]` if none
  - raw string `r"..."`; tag pattern `r"#\w+"` (`#` literal, `\w` word char, `+` one-or-more, stops at first non-word char)
  - link pattern `r"\[\[(.+?)\]\]"` — escaped brackets `\[`, `.` any char, greedy `.+` vs lazy `.+?`, capture group `( )` returns only inside
- Did NOT start the puzzle — parked to avoid overreach (thorough-over-speed)

### Puzzles Completed
- (none — concept + REPL drills only)

### Vocabulary Introduced
- bare expression, regex / regular expression, `re.findall`, raw string, word character, escaping, greedy vs lazy, capture group

### What He Struggled With
- Guessed output before running again (S24 pattern): said assignment "prints three lines"; predicted script would echo bare `text` — corrected only by running
- Ran with an unsaved file; ran `python3 scratch.py` from wrong folder (file was in `projects/`)
- `\w+` boundary on `#multi-word` — predicted it'd keep the `-word` (missed that `-` stops the match)

### What Felt Solid
- Read both errors correctly (SyntaxError vs NameError) unprompted
- Trusted his second instinct on the `# b` no-match case
- Got the greedy→lazy fix and full link pattern each on first guess; clean explain-back (pattern vs exact match; `?` = "one or more but as few as possible")

### Where to Start Next Session
- ROADMAP Step 4 PUZZLE — `find_tag.py`: tag from `sys.argv[1]`, scan `.md` files in copy-vault (`os.listdir`), `re.findall` inside each, report which notes match
- Combines S30 (`sys.argv`) + S31 (`os.listdir` scan) + today (regex) — watch for backwards assignment + block placement
- Feeds BUILD 1 (tag finder)
