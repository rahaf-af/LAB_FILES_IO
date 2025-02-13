import json
from datetime import datetime
toDoListFile="toDo.json"

def read_tasks():
   try:
      with open(toDoList_file,"r",encoding="utf-8")as file:
         return json.load(file)
   except(fileNotFound, json.jsonEcodeEror):
      return[]

def save_task():
   with open(toDoList_file,"w",encoding="utf-8")as file:
    json.dump(tasks ,file, indent=4)

def add_task():
   title=input("enter the task title please").strip()
   dateAndTime=input("ente the date pleas (YYYY-MM-DD HH:MM:SS):").strip()
   task{"Title": title, "Date and time":dateAndTime,"Done":False}

   tasks= read_tasks()
   tasks.append(task)
   save_task(tasks)
   print("you added the task successfuly \n")


def list_tasks():
   tasks=read_tasks()
   if not tasks:
      print("no tasks was found")
      return
   print("\nyour tp do list is :")
   for i in enumerate(tasks,1):
      status="done" if task["done"] else "not done"
      print(f-"{i}-{task['title']}" -"{task['date and time']}"-"{'status'}")


def task_done() :
   list_tasks()
   tasks=read_tasks()
   try:
      task_num=int(input)
