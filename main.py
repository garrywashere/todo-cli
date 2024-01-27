# Made with ❤️ by Garry
# 27/01/24

from InquirerPy import inquirer, separator
import platform, tabulate, getpass, os
from database import database

clear = lambda: os.system("cls") if os == "Windows" else os.system("clear")

db = database()

class menu:
    def main():
        clear()

        print(f"Welcome {getpass.getuser().capitalize()}\n")
        option = inquirer.select(
            message = "What would you like to do?",
            choices = [
                "Show Tasks", # 0
                "Add New Task", # 1
                "Edit a Task", # 2
                separator.Separator(),
                "Mark Task as Done/Delete", # 4
                separator.Separator(),
                "Exit." # 6
        ]
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

            case _:
                print("Error")
                menu.main()

class tasks:
    def show():
        pass

    def add():
        pass

    def edit():
        pass

    def delete():
        pass

if __name__ == "__main__":
    try:
        menu.main()
    except Exception as e:
        print("An error occured:", e)