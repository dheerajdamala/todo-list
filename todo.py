import mysql.connector

# Connect to MySQL database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="d.dheeraj_127",
    port="3306",
    database="python_connect"
)

myc = mydb.cursor()

# Create the 'tasks' table if it doesn't exist
myc.execute("""
CREATE TABLE IF NOT EXISTS tasks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    description VARCHAR(255) NOT NULL,
    status VARCHAR(20) DEFAULT 'Pending'
)
""")

# Functions for the To-Do List
def add_task():
    description = input("Enter task description: ")
    query = "INSERT INTO tasks (description) VALUES (%s)"
    myc.execute(query, (description,))
    mydb.commit()
    print("Task added successfully.")

def view_tasks():
    query = "SELECT * FROM tasks"
    myc.execute(query)
    tasks = myc.fetchall()
    if tasks:
        print("\nYour Tasks:")
        for task in tasks:
            print(f"{task[0]}. {task[1]} - {task[2]}")
    else:
        print("\nNo tasks found.")

def update_task():
    view_tasks()
    task_id = input("Enter the task ID to update: ")
    new_description = input("Enter new description (or press Enter to skip): ")
    new_status = input("Enter new status (Pending/Completed): ").capitalize()

    if new_description:
        query = "UPDATE tasks SET description = %s WHERE id = %s"
        myc.execute(query, (new_description, task_id))
    if new_status:
        query = "UPDATE tasks SET status = %s WHERE id = %s"
        myc.execute(query, (new_status, task_id))
    mydb.commit()
    print("Task updated successfully.")

def delete_task():
    view_tasks()
    task_id = input("Enter the task ID to delete: ")
    query = "DELETE FROM tasks WHERE id = %s"
    myc.execute(query, (task_id,))
    mydb.commit()
    print("Task deleted successfully.")

def main():
    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            update_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

# Close the cursor and connection
myc.close()
mydb.close()