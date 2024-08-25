tasks = []


def add():
    
    job = input("Enter the task you would like to add to the list: ").upper()
    status = f"{job} I"
    tasks.append(status)
    print(f"{job} has been added to the To Do List.")


def view():

    if tasks == []:
        print("There are currently no tasks in the To Do List.")
    else: 
        print("\nVIEWING TO-DO LIST:\n(I stands for Incomplete)")
        for item in tasks:
            print(item)


def mark():

    try:
        print("TO-DO LIST:\n(I stands for Incomplete)")
        for item in tasks:
            print(item)
        completed_task = input("Type out the exact line of the task you want to mark complete, including the 'I' or 'It's done!' after the task.").upper()
        tasks.remove(completed_task)
        tasks.append(f"{completed_task}t's done!")
        print(f"{completed_task} has been marked complete.")

    except ValueError:
        print("Please type out the entire name of the task you want to mark complete, including the I after the task.")



def delete():
    
    try:
        if tasks == []:
            print("There are no tasks in the list to delete.")
        else:
            print("\nTO-DO LIST:\n(I stands for incomplete)")
            for item in tasks:
                print(item)
            deleted_task = input("Type out the entire name of the task you would like to delete, including the I after the task.").upper()
            tasks.remove(deleted_task)
            print(f"{deleted_task} has been deleted.")
            

    except ValueError:
        print("Make sure you type the number of the task you would like to delete.")



print("\nWelcome to the To-Do List App!")

while True:
    
    print("\nMenu:\n")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Mark a task as complete")
    print("4. Delete a task")
    print("5. Quit")

    try:
        choice = int(input("\nPlease enter the number of the action you would like to perform: "))
        if choice == 1: 
            add()
        elif choice == 2:
            view()
        elif choice == 3:
            mark()
        elif choice == 4:
            delete()
        elif choice == 5:
            break
    except ValueError:
        print("Please be sure to enter the number of the action.")
    finally:
        print("Thank you for using the to do list app!")
