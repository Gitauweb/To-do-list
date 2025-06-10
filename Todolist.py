def to_do_list():
    tasks = []  

    while True:
        print("To-Do List Menu:")
        print("1. Add task")
        print("2. Remove task")
        print("3. Show tasks")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter task: ")
            tasks.append(task)  
            print(f'Task "{task}" added ')

        elif choice == "2":
            task = input("Enter task to remove: ")
            if task in tasks:
                tasks.remove(task)
                print(f'Task "{task}" removed !')
            else:
                print("Task not found!")

        elif choice == "3":
            if not tasks:
                print(" to do list is empty broo !")
            else:
                print("Your To-Do List:")
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. {task}")

        elif choice == "4":
            print("Thank you!")
            break

        else:
            print("invalid ")


to_do_list()
