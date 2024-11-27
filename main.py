from datetime import datetime
import pytz
import json

options = {"create","update","mark-done","list","delete"}
#reading JSON file
with open('tasks.json','r') as openfile:
    tasks = json.load(openfile)

#code to assign key values for every new task
keys=list(tasks.keys())
current = int(keys[len(keys)-1])+1

#taking input from the user
print(options)
x = str(input("select option:" )).lower()

##coditions according to the input
if x=="list":
    print(tasks)

elif(x=="create"):
    y=str(input("add task:"))
    tasks[current] =  {
        "name": y,
        "completed": False,
        "time_created":str(datetime.now(pytz.timezone('Asia/Kolkata')))
    }

elif x=="delete":
    d=str(input("enter the number of task to delete "))
    del tasks[d]

elif(x=="mark-done"):
    z = str(input("type task id for complition:"))
    tasks[z]["completed"]=True

elif x == "update":
    print(tasks)
    num=str(input("enter the number of the task want to update :"))
    nam=str(input("enter the new name of the task:"))
    tasks[num]["name"] = nam
    
else:
    print("invalid input")

#saving tasks to the JSON file
json_object = json.dumps(tasks , indent=4)
with open("tasks.json","w") as outfile:
    outfile.write(json_object)

