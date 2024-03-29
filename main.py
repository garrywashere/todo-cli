# Made with ❤️ by Garry
# 27/01/24

# Import required Modules
import platform, tabulate, argparse, getpass, os
from InquirerPy import inquirer, separator
from database import database

# Setup parser for extra options
parser = argparse.ArgumentParser(description='A Command-Line To-Do app, written in Python 🐍.')
parser.add_argument('--godmode', action='store_true', help='Enable dangerous options')
args = parser.parse_args()
godmode = args.godmode

# Setup a clear command that works on all OSes
clear = lambda: os.system("cls") if os == "Windows" else os.system("clear")

# Initialise database
db = database()

class menu:
    def main():
        clear()

        print(f"Welcome {getpass.getuser().capitalize()}\n")
        options = [
                "Show Tasks", # 0
                "Add New Task", # 1
                "Edit a Task", # 2
                separator.Separator(),
                "Mark Task as Done/Delete", # 4
                separator.Separator(),
                "Exit." # 6
        ]

        if godmode:
            options.append(separator.Separator())
            options.append("CLEAR ALL")

        option = inquirer.select(
            message = "What would you like to do?",
            choices = options
        ).execute()

        match option:
            case "Show Tasks":
                tasks.show()

            case "Add New Task":
                tasks.add()

            case "Edit a Task":
                tasks.edit()

            case "Mark Task as Done/Delete":
                tasks.delete()

            case "Exit.":
                print("Goodbye!")
                db.end()
                clear()
                exit()

            case "CLEAR ALL":
                tasks.clear_all()

            case _:
                print("Error")
                menu.main()

class tasks:
    def show(): # Request a list of tasks from database.py, then display them in a table
        tasks = db.task_list()
        print(
            tabulate.tabulate(tasks, headers = ["Title", "Description", "Created/Edited"]),
        )
        input("\nPress Enter.")
        menu.main()

    def add(): # Add a task to the database
        title = ""
        while not title:
            title = inquirer.text(
                message = "Title:",
            ).execute()
        description = inquirer.text(
            message = "Description:"
        ).execute()

        try:
            db.task_add(title, description)

            input("\nTask Added.")
            menu.main()
        except Exception as e:
            print("\nCannot add task:", e)

            tasks.add()

    def edit(): # Lookup existing titles in the database and edit them
        title = tasks.search()
        print("\nLeave blank for no change.")
        new_title = inquirer.text(
                message = "New Title:",
            ).execute()
        if new_title:
            db.task_edit(db.lookup_by_title(title), new_title, "")
        description = inquirer.text(
            message = "New Description:"
        ).execute()
        if description:
            db.task_edit(db.lookup_by_title(title), "", description)

        input("\nTask Edited.")
        menu.main()

    def delete(): # Delete tasks or "Mark as Done"
        db.task_del(db.lookup_by_title(tasks.search()))

        input("\nTask Deleted.")
        menu.main()

    def search(): # Internal search function for delete and edit
        tasks = [task[0] for task in db.task_list()]
        if not tasks:
            input("\nNo Tasks.")
            menu.main()
        else:
            task = inquirer.fuzzy(
                message = "Select a task to Delete:",
                choices = tasks
            ).execute()
        
        return task

    def clear_all(): # Hidden option for testing/debug purposes
        print("THIS WILL CLEAR THE DATABASE,")
        option = inquirer.confirm(
            message = "ARE YOU SURE?"
        ).execute()
        if option:
            db.drop()
            input("\nTable Dropped.")
        menu.main()

if __name__ == "__main__":
    try:
        menu.main()
    except Exception as e:
        print("An error occured:", e)