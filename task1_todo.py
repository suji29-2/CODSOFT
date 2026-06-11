tasks = []

priority_order = {"High": 1, "Medium": 2, "Low": 3}

while True:
    print("\n1.Add Task")
    print("2.View Tasks")
    print("3.Delete Task")
    print("4.Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Task Name: ")
        priority = input("Priority (High/Medium/Low): ")
        due = input("Due Date (DD-MM-YYYY): ")

        tasks.append({
            "name": name,
            "priority": priority,
            "due": due
        })

    elif choice == "2":
        sorted_tasks = sorted(
            tasks,
            key=lambda x: priority_order.get(x["priority"], 4)
        )

        for i, task in enumerate(sorted_tasks, start=1):
            print(f"{i}. {task['name']} | {task['priority']} | {task['due']}")

    elif choice == "3":
        num = int(input("Task Number: "))
        if 0 < num <= len(tasks):
            tasks.pop(num - 1)

    elif choice == "4":
        break