import pickle
import datetime as dt

# colors for terminal
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


f = open("./files/to_do_list.dat", "ab")

print("")
print(bcolors.OKBLUE + "Starting program...\n")
options = ["Create new list", "Read existing list", "Delete pervious list"]

def to_do():
    ## Presenting options to user
    for i in range(0,3):
        print("\t",i + 1, " --- ", options[i])
    # option selected
    option = int(input("Enter your option number: "))
    if option == 1:
        ## creating new list
        print("")
        print(bcolors.WARNING + "Creating new TO DO list...")
        d = dt.datetime.now()
        n = 1
        t_list = [d]
        while True:
            print(bcolors.BOLD + "Enter task no ", n)
            task = input("\tEnter your task: ")
            t_list.append(task)
            ans = input("Do you wish to enter more tasks (y/n)? : ")
            if ans.lower() in ["n", "no", "nope", "nah"]:
                print("Adding tasks...")
                break
        print(t_list)
        
to_do()
    


