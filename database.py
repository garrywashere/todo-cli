# Made with ❤️ by Garry
# 27/01/24

class database:
    def __init__(self):
        import sqlite3, time, os

        DB_FILE = "data.db"

        init_db = False
        if not os.path.exists(DB_FILE):
            init_db = True

        self.db = sqlite3.connect(DB_FILE)
        self.cursor = self.db.cursor()

        if init_db:
            self.cursor.execute("""
            CREATE TABLE tasks (
                task_id INTEGER PRIMARY KEY AUTOINCREMENT,
                task_title TEXT NOT NULL,
                task_desc TEXT,
                task_created REAL
            );
            """)
            self.db.commit()

    def task_list(self):
        tasks = self.cursor.execute("SELECT task_title, task_desc, task_created FROM tasks;").fetchall()

        results = []
        for task in tasks:
            results.append(task)
        
        return results

    def task_add(self, title, desc):
        if not desc:
            desc = "N/A"
        
        created = time.time()

        self.cursor.execute(f"""
        INSERT INTO tasks (task_title, task_desc, task_created)
        VALUES (\"{title}\",\"{desc}\",\"{created}\");""")

        self.db.commit()
    
    def task_del(self, id):
        try:
            self.cursor.execute(f"""
            DELETE FROM tasks WHERE task_id = \"{id}\";
            """)
            self.db.commit()
        except Exception as e:
            print("Error deleting task:", e)

    def task_edit(self, id, title, desc):
        try:
            if title:
                self.cursor.execute(f"""
                UPDATE tasks
                SET task_title = \"{title}\"
                WHERE task_id = \"{id}\";
                """)
            if desc:
                self.cursor.execute(f"""
                UPDATE tasks
                SET task_desc = \"{desc}\"
                WHERE task_id = \"{id}\";
                """)
            self.db.commit()
        except Exception as e:
            print("Error editing task:", e)
    
    def lookup_by_title(self, title):
        tasks = self.cursor.execute(f"""
        SELECT task_id, task_title, task_desc, task_created FROM tasks
        WHERE task_title = \"{title}\"
        """).fetchall()

        results = []
        for task in tasks:
            results.append(task)
        
        return results
        
    def lookup_by_id(self, id):
        tasks = self.cursor.execute(f"""
        SELECT task_id, task_title, task_desc, task_created FROM tasks
        WHERE task_id = \"{id}\"
        """).fetchall()

        results = []
        for task in tasks:
            results.append(task)
        
        return results
    
    def end(self):
        self.db.commit()
        self.db.close()

if __name__ == "__main__":
    print("nuh uh")
    exit()