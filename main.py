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
    
print("Press 1 for Creating a file")
print("Press 2 for Reading a file")
print("Press 3 for updating a file")
print("Press 4 for deletion a file")

check = int(input("PLease Enter your Chouce: "))

if check == 1:
    createfile()