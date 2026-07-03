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

**Pace:** thorough over speed (Dustin's rule, S30). Full REPL drills before every
concept, explain-backs that actually probe, and no advancing to the next build
until the current one is genuinely solid — even when a concept looks easy.

**Setup note:** Dustin has a **copy of his vault** to test on. Point all scripts —
including the write-builds — at the copy, so nothing risks the real vault.

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

> **New capability the write-builds add:** so far the script only *reads*. BUILD 2+
> **write a note back into the vault.** Two pieces, both from what he knows:
> a `[[link]]` is just a built string (`"[[" + filename-without-".md" + "]]"`), and
> "overwrite each run" is `open(path, "w")` (write mode wipes + rewrites — the reason
> it's `"w"` not `"a"`). An "empty note" = content that is `""` after `.strip()`.

### BUILD 1 — Tag finder (read-only foundation)
*Prereqs: steps 1–4. First real vault tool; the read-half of everything below.*
- [ ] Takes a tag as a command-line argument: `python3 find_tag.py "#Nuggets"`
- [ ] Scans every `.md` file in the (copy) vault folder
- [ ] Prints each note that contains the tag (filename, maybe a match count)
- [ ] Runs in the terminal; committed to GitHub

### BUILD 2 — Empty-note report (first write)
*Prereqs: BUILD 1. Smallest, safest write-build — teaches generating an output note.*
- [ ] Finds notes whose content is empty after `.strip()`
- [ ] Writes them as `[[links]]` into `Empty Notes.md`, one per line
- [ ] Overwrites the report each run (`"w"` mode)

### BUILD 3 — Tag MOC generator
*Prereqs: BUILD 2. Dustin's #Nuggets/#Exploration idea. ("MOC" = Map of Content, an auto-index note.)*
- [ ] `python3 moc.py "#Exploration"` → builds an overview note linking every note of that kind
- [ ] Each match becomes a `[[link]]` line; a count at the top (e.g. "17 notes")
- [ ] Overwrites the MOC note each run so it always reflects the current vault

### BUILD 4 — Vault Stats Report (alongside capstone)
*Prereqs: BUILDS 1–3. The useful-data overview — kept alongside the MOC per Dustin's ask.*
- [ ] Note count and total word count across the vault
- [ ] Top tags by frequency, and `[[links]]` counted **by name** (grouping/accumulator dict)
- [ ] Most-linked notes, most-referenced tags
- [ ] Prints a clean report to the terminal — stretch: write it to `VAULT_STATS.md`
- [ ] Runs in the terminal; committed to GitHub

---

## After Scripting
- `argparse` for nicer command-line tools (flags, help text) — stdlib
- Write-scripts that *modify* the vault (add frontmatter, bulk-rename) — with a dry-run first
- A "task inbox": collect every unfinished `- [ ]` task into one note (stretch build)
- A session log: append a dated line to a log note each run (`"a"` mode) — Dustin's idea
- Return to OOP when a script grows big enough to earn a class (`roadmaps/ROADMAP_oop_PAUSED.md`)

## Parked (set aside on purpose)
- OOP / writing your own classes — `roadmaps/ROADMAP_oop_PAUSED.md`
- GUI Expense Tracker (CustomTkinter) — `roadmaps/ROADMAP_expense_gui_PAUSED.md`
- Flask web walkthrough (a tour, explored not learned) — `roadmaps/ROADMAP_flask_walkthrough.md`
