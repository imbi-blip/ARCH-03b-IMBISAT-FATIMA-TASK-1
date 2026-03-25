import json

FILE = "tasks.json"

def load():
    try:
        return json.load(open(FILE))
    except:
        return []

def save(tasks):
    json.dump(tasks, open(FILE, "w"))

def show(tasks):
    if not tasks:
        print("No tasks.")
        return

    print("\nYour Tasks:")
    for i, t in enumerate(tasks):
        status = "Done" if t["done"] else "Not Done"
        print(f"{i+1}. {t['title']} [{status}]")

def mark_done(tasks):
    show(tasks)
    n = int(input("Task number: ")) - 1

    if 0 <= n < len(tasks):
        tasks[n]["done"] = True
        save(tasks)
        print("Task marked as done!")


tasks = load()

while True:
    print("\n1.Add  2.View  3.Mark Done  4.Exit")
    c = input("Choose: ")

    if c == "1":
        title = input("Task: ")
        tasks.append({"title": title, "done": False})
        save(tasks)

    elif c == "2":
        show(tasks)

    elif c == "3":
        mark_done(tasks)

    elif c == "4":
        break
