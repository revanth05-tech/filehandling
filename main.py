from os import name
from pathlib import Path
def readfileandfolder():
    path = Path()
    items = list(path.rglob('*'))
    for i,items in enumerate(items):
        print(f"{i+1} : {items}")

def createfile():
    try:
        readfileandfolder()
        filename = input("Please Enter your File Name: ")
        p = Path(filename)
        if not p.exists():
            with open(p,"w") as fs:
                data = input("What you want to write in this file: ")
                fs.write(data)
            print(f"File '{filename}' created successfully.")
        else:
            print(f"File '{filename}' already exists.")
    except Exception as e:
        print(f"An error occurred: {e}")

def readfile():
    try:    
        readfileandfolder()
        filename = input("Please Enter your File Name to Read: ")
        p = Path(filename)
        if p.exists() and p.is_file():
            with open(p,'r') as fs:
                data = fs.read()
                print(data)
            print("Readed Successfully")
        else:
            print(f"File '{filename}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

def updatefile():
    try:
        readfileandfolder()
        filename = input("Please Enter your File Name to Update: ")
        p = Path(filename)
        if p.exists() and p.is_file():
            with open(p,'a') as fs:
                data = input("What you want to append in this file: ")
                fs.write(data)
            print("Updated Successfully")
        else:
            print(f"File '{filename}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")


    
print("Press 1 for Creating a file")
print("Press 2 for Reading a file")
print("Press 3 for updating a file")
print("Press 4 for deletion a file")

check = int(input("PLease Enter your Chouce: "))

if check == 1:
    createfile()
    
if check == 2:
    readfile()

if check == 3:
    updatefile()
    