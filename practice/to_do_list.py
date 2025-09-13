class ToDoList:
    def __init__(self):
        self.__toDoList = []

    def add_task(self, task):
        if task not in self.__toDoList:
            self.__toDoList.append(task)
        else:
            print("Your task is in the to-do list")
    
    def remove_task(self, task):
        if task in self.__toDoList:
            self.__toDoList.remove(task)
        else:
            print("Failed: 'Your task is not in the list'")
    
    def modify_task(self, task):
        if task in self.__toDoList:
            modify = self.__toDoList.index(task)
            self.__toDoList[modify] = input("Type your modificaiont task: ")
        else:
            print("Failed: 'Your task is not in the list'")

    def show_all_tasks(self):
        if self.__toDoList:
            for task in self.__toDoList:
                print(task)
        else:
            print("You don't have any task")

todo_list = ToDoList()
# Task I add
print("----This is the beginning of the adding----")
todo_list.add_task('Learn introduction to database management system')
todo_list.add_task('Meta-backend developer')
todo_list.add_task('Django for backend development')
todo_list.add_task('Version Control : git & github')
todo_list.show_all_tasks()
# Task I remove
print("----This is the beginning of the removing---")
todo_list.remove_task('Learn introduction to database management system')
todo_list.remove_task('Introduction to front-end development')
todo_list.show_all_tasks()
# Task I modify
print("----This is the beginning of the modification----")
todo_list.modify_task('Virsion Control : git & github')
todo_list.modify_task('Version Control : git & github')
todo_list.show_all_tasks()