from datetime import datetime
import pytz
import json
options = {"create","update","mark-done","mark-in-progress","list","delete"}
with open('tasks.json','r') as openfile:
    tasks = json.load(openfile)
current = len(tasks)
print(options)
x = str(input("select option:" )).lower()

if x=="list":
    print(tasks)
elif(x=="create"):
    y=str(input("add task:"))
    tasks[current] =  {
        "name": y,
        "completed": False,
        "time_created":str(datetime.now(pytz.timezone('Asia/Kolkata')))
    }
    
elif(x=="mark-done"):
    z = str(input("type task id for complition:"))
    tasks[z]["completed"]=True
else:
    print("invalid input")

json_object = json.dumps(tasks , indent=4)
with open("tasks.json","w") as outfile:
    outfile.write(json_object)

