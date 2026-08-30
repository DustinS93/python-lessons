# Concept: using methods on list
tasks = ["run", "walk", "crawl"]
print(f"I have {len(tasks)} things to do today")
tasks.append("jump")
tasks.append("fly")
tasks.remove("run")
print(f"{tasks} now look at all I have to do today! That's {len(tasks)} things!")
print("That's too much...")
tasks.pop()
print(f"{tasks} now that's better! Only {len(tasks)} things!")
