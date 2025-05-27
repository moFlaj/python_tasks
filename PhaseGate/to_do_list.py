
def add_a_task(task):
	tasks.append(task)

def view_all_tasks(tasks):
	index = 1
	for task in tasks:
		print(f"{index}. {task}")
		index+=1

def delete_task(task):

	tasks.remove(task)

def mark_task_as_complete(task):
	
	tasks.append("[X]" + task)
	tasks.remove(task)
	

def menu_list():

	menu_list = """
	
To-do List Manager

1. Add a task
2. View all tasks
3. Mark a task as complete
4. Delete a task
5. Exit

"""
	
	return menu_list

def to_do_list_check(tasks):
	to_do = True
	while to_do:
		print(menu_list())
		user_input = input("Enter your choice: ")
		match user_input:
			case "1":
				user_task = input("Enter task: ")
				add_a_task(user_task)
				print("Task added")
				view_all_tasks(tasks)
				break
			case "2": 
				view_all_tasks(tasks)
				break
			case "3": 
				view_all_tasks(tasks)
				user_input = input("Enter your choice: ")
				mark_task_as_complete(user_input)
				print(tasks)
				break
			case "4": 
				view_all_tasks(tasks)
				user_input = input("Enter your choice: ")
				delete_task(user_input)
				print(tasks)
				break
			case "5":
				to_do = False
			case _: 
				print("Invalid input")
	
	view_all_tasks(tasks)

tasks = ["Run", "Jog"]
to_do_list_check(tasks)
	
		
		