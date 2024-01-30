# To-do App
A Command-Line To-Do app, written in Python 🐍.

## Introduction
Just a simple To-Do app; I decided to make this as part of a series of side projects to keep my skills sharp.

## Issues
- The app interacts with tasks by getting their id from the title. Multiple tasks sharing the same title may cause instability. However, I added a janky "fix" which includes setting the `task_title` column as unique. Upcoming solution is to change the way tasks are handled by only using their id for any kind of functions that modify the contents of the database.

## Features to Add
- Encryption
- Catch `KeyboardInterrupt`