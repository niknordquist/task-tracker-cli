from datetime import datetime
import json
        
def add(description):
    with open("todo.json", "r+") as file:
        try:
            tasks_file = json.load(file)
            task_list = tasks_file["tasks"]
            file.seek(0)
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
        
        
def welcomeMessage():
    print("Hello, welcome to the Task Tracker Command Line Prompt!")
    print("""Commands:\n\nadd <task info>\ndelete <task id>\nupdate <task id> <task info>
mark-in-progress <task id>\nmark-done <task id>\nlist done/todo/in-progress\nPress 'q' to quit\n""")

def main():
    welcomeMessage()
    endTrigger = False
    while endTrigger == False:
        userInput = input("Enter a command (Press 'q' to quit): ")
        currentCommand = userInput.split()
        match currentCommand[0]:
            case "add":
                add(currentCommand[1])
            case 'q':
                endTrigger = True
            case _:
                print("Invalid command!")
        

if __name__ == "__main__":
    main()
     