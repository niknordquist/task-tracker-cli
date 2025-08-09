from datetime import datetime
import json

def load_file(file):
    tasks_file = json.load(file)
    task_list = tasks_file["tasks"]
    file.seek(0)
        
def add(description):
    with open("todo.json", "r+") as file:
        try:
            load_file(file)
            data = {
                'id': len(task_list) + 1,
                'description': description,
                'status': "Todo",
                'createdAt': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'updatedAt': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            task_list.append(data)
            json.dump(tasks_file, file)
        except Exception as e:
            print(f'Failed to create new task. Error: {e}')
            
def delete(id):
    pass

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
                    delete(currentCommand[1])
                case "update":
                    update(currentCommand[1], currentCommand[2])
                case "mark-in-progress":
                    mark_in_progress(currentCommand[1])
                case "mark-done":
                    mark_done(currentCommand[1])
                case "list":
                    list_tasks() if len(currentCommand) < 2 else list_tasks(currentCommand[1])
                case 'q':
                    endTrigger = True
                case _:
                    print("Invalid command!")
        except IndexError as ioe:
            print("Command failed, please provide the correct format in your command.")

if __name__ == "__main__":
    main()
     