# ROADMAP.md — Core Python: Scripting (terminal + Obsidian-vault tools)

## The Point
Turn Python into something **useful in real life** — small scripts that run from
the terminal and do real work on Dustin's Obsidian vault (a folder of plain-text
`.md` files). The end goal he named: **pull useful stats/data out of the vault.**

Still **pure Python, stdlib only** — no third-party libraries. Everything runs in
plain `python3`. The new tools this track introduces are all built in: `sys`
(command-line arguments), `os` (walking a folder of files), and `re` (regex
pattern-matching for tags and `[[links]]`).

**Why scripting now:** Dustin uses Obsidian daily and wants Python to earn its
keep. This is his "build something real." It reuses what's already solid —
**file I/O, string methods, dicts, the grouping/accumulator pattern** — and adds
the handful of new skills that separate a *puzzle* from a *tool you run*.

**What a vault script can/can't do** (mental model, set S30):
- CAN: read/scan the whole vault folder, search & extract text (tags, links,
  tasks), count things, generate reports, create/rewrite/rename files.
- CAN'T (pure Python): touch the live Obsidian app, graph, or rendering — that's
  the JS plugin world. The script only sees files on disk, and only knows what a
  "tag" or "link" is because you code that rule.
- GOTCHA: run write-scripts with Obsidian **closed**; read-only scans are safe anytime.

**OOP is parked** (`roadmaps/ROADMAP_oop_PAUSED.md`) — understood fundamentally,
resume later on request.

---

## How to Read This
Same format as always:
- **Learn** steps: REPL drill + puzzle. Both checked before moving on.
- **Build** is the milestone — a running pure-Python script.
- At session start, scan for the first unchecked box.

**Setup note:** builds need a folder of `.md` files. Point at the real vault for
read-only scans, or make a small `test_vault/` folder of sample notes to
experiment safely first.

---

## Steps

### 1. Run a script from the terminal + take an argument
*Teaches: `python3 script.py`, `sys.argv`, `if __name__ == "__main__":`*
- [ ] REPL/drill — `import sys; sys.argv` (what the list holds; `argv[0]` vs `argv[1]`)
- [ ] Puzzle — `greet.py`: run `python3 greet.py Dustin` and it prints `Hello, Dustin`
      (reads the name from the command line, not `input()`)

### 2. Read a file whose path comes from the command line
*Teaches: opening a path passed as an argument; script works on any file*
- [ ] REPL/drill — `open(sys.argv[1])`, read it, print it
- [ ] Puzzle — `wordcount.py`: `python3 wordcount.py notes.md` prints the word count
      (reuses `.read()` / `.split()`)

### 3. Scan a whole folder of files
*Teaches: `os.listdir`, filtering with `.endswith(".md")`, `os.path.join`*
- [ ] REPL/drill — list a folder, keep only `.md` files, build full paths
- [ ] Puzzle — `list_notes.py`: print every `.md` filename in a vault/test folder

### 4. Search & extract patterns inside files
*Teaches: `in` / `.startswith` for simple matches; intro `re.findall` for `#tags` and `[[links]]`*
- [ ] REPL/drill — `re.findall(r"#\w+", text)` and `re.findall(r"\[\[(.+?)\]\]", text)`
- [ ] Puzzle — `find_tag.py` (feeds BUILD 1): given a tag, report which notes contain it

---

### BUILD 1 — Tag finder (CLI, no libraries)
*Prereqs: steps 1–4. First real vault tool.*
- [ ] Takes a tag as a command-line argument: `python3 find_tag.py "#idea"`
- [ ] Scans every `.md` file in the vault folder
- [ ] Prints each note that contains the tag (filename, maybe a match count)
- [ ] Runs in the terminal; committed to GitHub

### BUILD 2 — Link counter
*Prereqs: BUILD 1. Building block for the stats report. Leans on the grouping/accumulator dict.*
- [ ] Scans the vault, extracts every `[[link]]` target with `re.findall`
- [ ] Tallies counts **by name** in a dict: `counts[name] = counts[name] + 1`
- [ ] Prints each linked note and how many times it's referenced (most-linked first)

### BUILD 3 — Vault Stats Report (capstone)
*Prereqs: BUILDS 1–2. The thing he actually wants: useful data about the vault.*
- [ ] Note count and total word count across the vault
- [ ] Top tags by frequency (grouping/accumulator)
- [ ] Most-linked notes (reuses BUILD 2)
- [ ] Prints a clean report to the terminal — stretch: write it to `VAULT_STATS.md`
- [ ] Runs in the terminal; committed to GitHub

---

## After Scripting
- `argparse` for nicer command-line tools (flags, help text) — stdlib
- Write-scripts that *modify* the vault (add frontmatter, bulk-rename) — with a dry-run first
- A "task inbox": collect every unfinished `- [ ]` task into one note (stretch build)
- Return to OOP when a script grows big enough to earn a class (`roadmaps/ROADMAP_oop_PAUSED.md`)

## Parked (set aside on purpose)
- OOP / writing your own classes — `roadmaps/ROADMAP_oop_PAUSED.md`
- GUI Expense Tracker (CustomTkinter) — `roadmaps/ROADMAP_expense_gui_PAUSED.md`
- Flask web walkthrough (a tour, explored not learned) — `roadmaps/ROADMAP_flask_walkthrough.md`
