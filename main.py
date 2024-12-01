from datetime import datetime
from prettytable  import PrettyTable
import pytz
import json

#giving options to select 
options = {"create","update","mark-done","list","delete"}
opt = PrettyTable()
opt.field_names=["options"]
for o in options:
    opt.add_row([o])



#reading JSON file
with open('tasks.json','r') as openfile:
    tasks = json.load(openfile)

#code to assign key values for every new task
keys=list(tasks.keys())
current = int(keys[len(keys)-1])+1

#taking input from the user
print(opt)
x = str(input("select option: " )).lower()

#listing in tabular format
table = PrettyTable()
table.field_names = ["task no","task title","completed","time created"]
for key in tasks:
    table.add_row([key,tasks[key]["name"],tasks[key]["completed"],tasks[key]["time_created"]])

##coditions according to the input
if x=="list":
    print(table)

elif(x=="create"):
    y=str(input("add task:"))
    tasks[current] =  {
        "name": y,
        "completed": False,
        "time_created":str(datetime.now(pytz.timezone('Asia/Kolkata')))
    }
    print("your new task is added.")

elif x=="delete":
    print(table)
    d=str(input("enter the number of task to delete "))
    del tasks[d]

elif(x=="mark-done"):
    print(table)
    z = str(input("type task id for complition:"))
    tasks[z]["completed"]=True

elif x == "update":
    print(table)
    num=str(input("enter the number of the task want to update :"))
    nam=str(input("enter the new name of the task:"))
    tasks[num]["name"] = nam
    
else:
    print("invalid input")

#saving tasks to the JSON file
json_object = json.dumps(tasks , indent=4)
with open("tasks.json","w") as outfile:
    outfile.write(json_object)