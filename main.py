from datetime import datetime
import json

def getNextID():
    with open("id.txt", "r+") as file:
        id_file = json.load(file)
        file.seek(0)
        id = int(id_file)
        id += 1
        json.dump(id, file)
        return id 
        
def add(description):
    with open("todo.json", "r+") as file:
        try:
            tasks_file = json.load(file)
            file.seek(0)
            data = {
                'id': getNextID(),
                'description': description,
                'status': "Todo",
                'createdAt': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'updatedAt': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            tasks_file.append(data)
            json.dump(tasks_file, file)
            print(f'Task: {description} with ID {data["id"]} added!')
        except Exception as e:
            print(f'Failed to create new task. Error: {e}')
            
def delete(id):
    global totalTasks
    with open("todo.json", "r+") as file:
        try:
            tasks_file = json.load(file)
            file.seek(0)
            tasks_file = [val for val in tasks_file if val['id'] != id]
            json.dump(tasks_file, file)
            file.truncate()
            print(f'Deleted task with ID {id}!')
        except Exception as e:
            print(f'Failed to delete task with id {id}: {e}')

def update(id, description):
    pass

def mark_in_progress(id):
    pass

def mark_done(id):
    pass

def list_tasks(status = "all"):    
    pass    
        
def welcomeMessage():
    print("Hello, welcome to the Task Tracker Command Line Prompt!")
    print("""Commands:\n\nadd <task info>\ndelete <task id>\nupdate <task id> <task info>
mark-in-progress <task id>\nmark-done <task id>\nlist done/todo/in-progress\nPress 'q' to quit\n""")

def main():
    welcomeMessage()
    endTrigger = False
    while endTrigger == False:
        try:
            userInput = input("Enter a command (Press 'q' to quit): ")
            currentCommand = userInput.split()
            if len(currentCommand) > 2: raise IndexError
            match currentCommand[0]:
                case "add":
                    add(currentCommand[1])
                case "delete":
                    delete(int(currentCommand[1]))
                case "update":
                    update(int(currentCommand[1]), currentCommand[2])
                case "mark-in-progress":
                    mark_in_progress(int(currentCommand[1]))
                case "mark-done":
                    mark_done(int(currentCommand[1]))
                case "list":
                    list_tasks() if len(currentCommand) < 2 else list_tasks(currentCommand[1])
                case 'q':
                    endTrigger = True
                case _:
                    print("Invalid command!")
        except IndexError as ioe:
            print("Command failed, please provide the correct format in your command.")
        except ValueError as ve:
            print("Command failed, task ID must be an integer")

if __name__ == "__main__":
    main()
     