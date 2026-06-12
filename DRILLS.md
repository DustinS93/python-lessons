# DRILLS.md — Running Reference

## Vocabulary

| Term | Definition |
|---|---|
| parameter | The placeholder name in a function definition — `def greet(name)`, `name` is the parameter |
| argument | The actual value you pass when calling a function — `greet("Dustin")`, `"Dustin"` is the argument |
| default parameter | A parameter with a fallback value — `def greet(name, animal="dog")`. Must come after non-default parameters |
| keyword argument | Passing an argument by name when calling a function — `greet(greeting="Hi", name="Dustin")`. Order doesn't matter when you use the name |
| return value | The value a function hands back to the caller via `return`. Distinct from printing |
| truncation | Cutting off the decimal without rounding — `int(7.9)` gives `7`, not `8` |
| REPL | Read, Evaluate, Print, Loop — the interactive Python shell (`python3` in terminal) |
| conditional | A statement that runs code only if a condition is true — `if`, `elif`, `else` |
| elif | Short for "else if" — checks a new condition only if the previous one was false |
| scope | Where a variable exists and can be accessed |
| local scope | Inside a function — variables defined here only exist for the life of that function call |
| global scope | Outside all functions — visible everywhere in the file, including inside functions |
| index | The position of an item in a list. Starts at `0`. `list[0]` is the first item |
| negative index | Counting from the end of a list. `list[-1]` is always the last item |
| key | The label used to access a value in a dictionary — `person["name"]`, `"name"` is the key |
| value | The data stored at a key in a dictionary — `person["name"]` returns `"Dustin"`, the value |
| key-value pair | One entry in a dictionary — a key and its associated value, e.g. `"age": 30` |
| `None` | Python's built-in value for "nothing" — capital N. Returned by functions that don't explicitly return a value. `none` (lowercase) doesn't exist and raises a `NameError` |
| case-sensitive | Python distinguishes uppercase from lowercase — `None` and `none` are completely different. Same for variable names, keywords, everything |

---

## Concepts, Methods & Functions

### Functions
- `def function_name(parameter):` — defines a function
- `return` — hands a value back to the caller and exits the function immediately
- `print()` — displays output to the screen, does not hand a value back (returns `None`)
- Default parameters: `def greet(name, animal="dog")` — fallback used when no argument is passed
- Functions calling functions: `print(format_share(bill_splitter(100, 4)))`
- Passing a return value as an argument: the inner function runs first, its result is passed to the outer

### Type Conversion
- `str(x)` — converts `x` to a string. Required when concatenating a number with a string
- `int(x)` — converts `x` to an integer. Truncates decimals, does not round
- `float(x)` — converts `x` to a float (decimal number)
- `int(float("7.5"))` — chain conversions when needed. `int("7.5")` alone raises a `ValueError`
- `int(input())` — wrap `input()` to convert user input at the source

### Input
- `input("prompt")` — displays a prompt, pauses the program, returns whatever the user types **as a string**, always

### Conditionals
- `if` / `elif` / `else` — Python checks top to bottom and stops at the first true condition
- `>` strictly greater than, `>=` greater than or equal to (same logic for `<` and `<=`)
- If no condition is true and there's no `else`, nothing happens — not an error
- Redundant `elif` conditions: if `score >= 90` already failed, `score >= 80` doesn't need to re-check the upper bound

### Scope
- Local variable: defined inside a function, only exists there. Accessing it outside raises `NameError`
- Global variable: defined outside functions, readable inside functions
- Same name in two scopes: the function uses its own local copy — the global is unchanged
- `return` vs `print` inside a function: `print()` shows output but returns `None`. `return` hands the value back

### Lists
- Creating a list: `items = ["apple", "banana", "cherry"]`
- Indexing: `items[0]` → first item, `items[1]` → second, `items[-1]` → last item
- `len(items)` — returns the number of items in the list
- `for item in items:` — loops through each item one at a time. The loop variable (`item`) is a temporary name you choose — it can be anything
- `list.append(item)` — adds `item` to the end of the list
- `list.pop()` — removes and returns the last item in the list
- `list.remove(item)` — removes the first occurrence of `item` from the list (by value, not index)
- `item in list` — returns `True` if `item` is in the list, `False` otherwise

### Loops
- Loop counter pattern — set a variable before the loop, update it inside:
  ```python
  number = 0
  for i in items:
      number = number + 1
  ```
- `return` inside a loop exits the **entire function**, not just the current iteration
- Loop variable name is arbitrary — `for x in items` and `for item in items` behave identically
- `while condition:` — runs as long as the condition is true. You are responsible for updating the condition inside the loop or it runs forever
- Code after a `while` block runs once when the loop ends — good place for a final action like `print("Blast Off!")`
- `while True:` — loops forever intentionally. Use `break` to escape from inside when a condition is met
- `break` — exits the current loop entirely. Different from `return` (exits the function) and `continue` (skips to next iteration)
- Use `while True` when you don't have a value to check yet at the start of the loop — define the value inside, then check it with `if` + `break`

### Dictionaries
- Creating a dictionary: `person = {"name": "Dustin", "age": 30}`
- Accessing a value: `person["name"]` → `"Dustin"`
- Adding a key: `person["job"] = "developer"` — creates the key if it doesn't exist
- Updating a key: `person["age"] = 99` — overwrites the existing value
- `KeyError` — raised when you access a key that doesn't exist
- `len(dict)` — returns the number of key-value pairs
- `dict.keys()` — returns all keys in the dictionary
