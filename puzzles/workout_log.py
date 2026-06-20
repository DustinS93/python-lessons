# Concept: saving and loading a list of dicts to/from a file using comma-seperated lines
import os
log = []
if os.path.exists("workout_log.txt"):
    with open("workout_log.txt", "r") as f:
        contents = f.readlines() 
        for line in contents:
            parts = line.strip().split(",")
            log.append({"exercise": parts[0], "sets": int(parts[1]), "reps": int(parts[2])})


print("--- WORKOUT LOG ---")
number = 0
for l in log:
    number = number + 1
    print(str(number) + ". " + l["exercise"])
print("New Entry:")
log.append({"exercise": input("Exercise name: "), "sets": input("How many sets?: "), "reps": input("How many reps per set?: ")})
with open("workout_log.txt", "w") as f:
    for i in log:
        f.write(i["exercise"] + "," + str(i["sets"]) + "," + str(i["reps"]) + "\n")
print("SAVED")