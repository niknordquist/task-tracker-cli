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
    with open("todo.json", "r+") as file:
        try:
            tasks_file = json.load(file)
            file.seek(0)
            for task in tasks_file:
                if task["id"] == id:
                    task["description"] = description
                    json.dump(tasks_file, file)
                    file.truncate()
                    print(f'Updated task with ID {id}!')
                    return
            print(f'Could not find task with ID {id}')
        except Exception as e:
            print(f'Failed to delete task with id {id}: {e}')

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
            command = userInput.split(maxsplit=1)[0]
            match command:
                case "add":
                    add(userInput.split(maxsplit=1)[1])
                case "delete":
                    delete(int(userInput.split(maxsplit=1)[1]))
                case "update":
                    update(int(userInput.split(maxsplit=2)[1]), userInput.split(maxsplit=2)[2])
                case "mark-in-progress":
                    mark_in_progress(int(userInput.split(maxsplit=1)[1]))
                case "mark-done":
                    mark_done(int(userInput.split(maxsplit=1)[1]))
                case "list":
                    pass
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
     