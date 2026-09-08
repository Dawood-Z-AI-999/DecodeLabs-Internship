final_list = []

while True:
    print("\n-----Todo List-----")
    print("1. enter the task")
    print("2. View your task")
    print("3. Exit Program")

    choice = input("Pick the option (1-3): ")

    if choice  == "1":
        user_todo = input("Enter your To-Do: ")
        final_list.append(user_todo)
        print("Task added...")

    elif choice == "2":
        print("\nYour Tasks:")
        for i, task in enumerate(final_list, start=1):
            print(f"{i}. {task}")  

    elif choice == "3":
        print("program Exited...")
        break  
    else:
        print("Invalid choice, try again!")

