from datetime import datetime
import json

totalTasks = 0
        
def add(description):
    with open("todo.json", "w") as file:
        try:
            data = {
                'id': totalTasks + 1,
                'description': description,
                'status': "Todo",
                'createdAt': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'updatedAt': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            json.dump(data, file)
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
     