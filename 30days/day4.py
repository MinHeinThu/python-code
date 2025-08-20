"""
Day 4 Project: To-Do List App (Simple Version)
🎯 Goal
Practice lists and loops
Learn to add, view, and delete items
Handle user choices with a menu system
Project Description
Build a command-line to-do list manager.
The user can:
Add a new task
View all tasks
Delete a task by number
Exit the program
"""
print('To-Do List App')
tasks = []
while True:
    task_action = input('Enter Task Action["add", "view", "delete", "modify", "exit"]: ')
    # Add methods
    if task_action.lower() == 'add':
        try:
            tasks.append(str(input('Add Task: ')))
            print('Task Added')
        except ValueError:
            print('Invalid input')
    # Views methods 
    elif task_action.lower() == 'view':
        # if task is emptmy show
        if not tasks:
            print('No tasks yet.')
        else:
            print('Your tasks:')
            for i, task in enumerate(tasks, 1):
                print(f'{i}. {task}')
    # Delete methods
    elif task_action.lower() == 'delete':
        if not tasks:
            print('No Task to delete')
        else:
            try:
                for i, task in enumerate(tasks, 1):
                    print(f'{i}, {task}')
                    num = (input('Enter task number to delete: '))
                    if 1 <= num and len(tasks) <= num:
                        removed = tasks.pop(num-1)
                        print('Task removed')
            except ValueError:
                print('You input is invalid')
    elif task_action.lower() == 'modify':
        if not tasks:
            print('No task to modify')
        else:
            for i, task in enumerate(tasks, 1):
                    print(f'{i}, {task}')
            try:
                modify = int(input('Enter the number modify the task:'))
                if modify >= 1 and modify <= len(tasks):
                    tasks[modify-1] = input('Modify the task: ')
                    print('Task modified')
            except ValueError:
                print('Enter a valid task number.')
    elif task_action.lower() == 'exit':
        print('Goodbye👏')
        break
    else:
        print('Your task action is invalid')
