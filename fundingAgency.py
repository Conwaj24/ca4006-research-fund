import sys
import os
import time
import glob
from tokenize import group

for line in sys.stdin:
    inp = line.split()
    command = inp[0]
    if command == "apply":
        group_name = inp[1]
        amount = inp[2]
        if (int(amount) < 200000 or int(amount) > 500000):
            print("Application for funding must be between 200,000 and 500,000, please try again.")
        
        else:
            with open("data/groups/" + group_name + "_balance", "w") as file:
                os.system('./withdraw ' + amount + " data/fa_balance")
                file.write(amount)
            with open("data/groups/" + group_name + "_names", "w") as file:
                file.write("")

            print("your application was successful, please add researchers\n")

    elif command == "withdraw":
        amount = inp[1]
        group_name = inp[2]
        researcher_name = inp[3]

        with open("data/groups/" + group_name + "_names") as researchers:
            name = researchers.readline().strip()
            while (name != researcher_name) and (name != ""):
                name = researchers.readline().strip()
            
            if (name == researcher_name):
                os.system('./withdraw ' + amount + " data/groups/"+group_name+"_balance")
            else:
                print("no such researcher " + name + " in group " + group_name)
        print("funds processed\n")

    elif command == "add_researcher":
        group_name = inp[1]
        researcher_name = inp[2]
        with open("data/groups/" + group_name + "_names", "a") as researchers:
            researchers.write(researcher_name + "\n")
        print("researcher added\n")

    elif command == "add_title":
        group_name = inp[1]
        title = inp[2]
        with open("data/groups/" + group_name + "_title", "w") as file:
            file.write(title)
            print("Title added to group: " + group_name)

    elif command == "get_title":
        group_name = inp[1]
        with open("data/groups/" + group_name + "_title", "r") as file:
            print(title)

    elif command == "add_description":
        group_name = inp[1]
        description = inp[2:]
        with open("data/groups/" + group_name + "_description", "w") as file:
            file.write(" ".join(description))
        print("description added to group")
    
    elif command == "get_description":
        group_name = inp[1]
        with open("data/groups/" + group_name + "_description", "r") as file:
            print(file.read() + "\n")
    else:
        print("no such command")


