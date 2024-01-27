# Made with ❤️ by Garry
# 27/01/24

import platform, tabulate, argparse, getpass, os
from InquirerPy import inquirer, separator
from database import database

parser = argparse.ArgumentParser(description='A Command-Line To-Do app, written in Python 🐍.')
parser.add_argument('--godmode', action='store_true', help='Enable dangerous options')
args = parser.parse_args()
godmode = args.godmode

clear = lambda: os.system("cls") if os == "Windows" else os.system("clear")

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
    def show():
        tasks = db.task_list()
        print(
            tabulate.tabulate(tasks, headers = ["Title", "Description", "Created/Edited"]),
        )
        input("\nPress Enter.")
        menu.main()

    def add():
        title = ""
        while not title:
            title = inquirer.text(
                message = "Title:",
            ).execute()
        description = inquirer.text(
            message = "Description:"
        ).execute()

        db.task_add(title, description)

        input("\nTask Added.")
        menu.main()

    def edit():
        pass

    def delete():
        tasks = [task[0] for task in db.task_list()]
        if not tasks:
            input("\nNo Tasks.")
        else:
            task = inquirer.fuzzy(
                message = "Select a task to Delete:",
                choices = tasks
            ).execute()

            db.task_del(db.lookup_by_title(task))

            input("\nTask Deleted.")
        menu.main()


    def clear_all():
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