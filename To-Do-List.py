# Simple To-Do List Application

def view_tasks():
    try:
        with open("to-do-list.txt", "r", encoding = "utf-8") as file:
            lines = file.readlines()
        if lines == []:
            print("No tasks in the to-do list.")
        else:
            for i, line in enumerate(lines, start=1):
                print(f"{i}. {line.strip()}")
    except FileNotFoundError:
        print("File not found. No tasks to display.")


def add_task():
    task = input("Enter the task to add: ")
    try:
        with open ("to-do-list.txt", "a", encoding = "utf-8") as file:
            file.write(task + "\n")
        print(f'Task "{task}" added to the list.')
    except FileNotFoundError:
        print("File not found. Creating a new to-do list file.")


def remove_task():
    try:
        with open("to-do-list.txt", "r", encoding = "utf-8") as file:
            lines = file.readlines()
            if not lines:
                print("No tasks to remove.")
                return
        
        view_tasks()
        num = int(input("Enter the task number to remove: "))
        if 1 <= num <= len(lines):
            removed = lines.pop(num - 1)
            print(f'Task "{removed.strip()}" removed from the list.')

            with open("to-do-list.txt", "w", encoding = "utf-8") as file:
                file.writelines(lines)      
        else:
            print("Invalid task number.")
    
    except FileNotFoundError:
        print("File not found. No tasks to remove.")

        
def mark_task_completed():
    try:
        with open("to-do-list.txt", "r", encoding = "utf-8") as file:
            lines = file.readlines()
            if not lines:
                print("No tasks to mark as completed.")
                return
        
        view_tasks()
        num = int(input("Enter the task number to mark as completed: "))
        if 1 <= num <= len(lines):
            lines[num - 1] = lines[num - 1].strip() + " (Completed)\n"
            print(f'Task "{lines[num - 1].strip()}" marked as completed.')

            with open("to-do-list.txt", "w", encoding = "utf-8") as file:
                file.writelines(lines)      
        else:
            print("Invalid task number.")
    
    except FileNotFoundError:
        print("File not found. No tasks to mark as completed.")



def main():
    while True:
        print ("\nTo-Do List Menu")
        print ("1. View To-Do List")
        print ("2. Add Task")
        print ("3. Remove Task")
        print ("4. Mark Task Completed")
        print ("5. Exit")
        choice = input("Choose an option (1-5): ")

        if choice == "1":
            view_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            mark_task_completed()
        elif choice == "5":
            print("Exiting the To-Do List application...")
            break
        else:
            print("Invalid choice. Please try again.")
        
if __name__ == "__main__":
    main()
