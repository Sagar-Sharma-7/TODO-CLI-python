from ColorChalks import ColorChalks # pip install ColorChalks
import pickle
import datetime as dt


f = open("./files/to_do_list.dat", "ab")

print("")
print(ColorChalks.FCOLORS.BrightBlue + "Starting program...\n")
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
        print(ColorChalks.FCOLORS.BrightYellow + "Creating new TO DO list...")
        d = dt.datetime.now()
        n = 1
        t_list = [d]
        while True:
            print("Enter task no ", n)
            task = input("\tEnter your task: ")
            t_list.append(task)
            n += 1
            ans = input("Do you wish to enter more tasks (y/n)? : ")
            if ans.lower() in ["n", "no", "nope", "nah"]:
                print("")
                pickle.dump(t_list, f)
                print(ColorChalks.FCOLORS.BrightMagenta + "Tasks added to your list successfully...")
                break
    elif option == 2:
        try:
            with open("./files/to_do_list.dat", "rb") as file:
                while True:
                    data = pickle.load(file)
                    print("\tEmpty file...")
                    print("")
                    print(ColorChalks.FCOLORS.BrightGreen + "\tDate&Time : ", data[0])
                    for i in range(1, len(data)):
                        print("\t",i, " : ", data[i])
                
        except EOFError:
            print("Closing file...")
            pass
    elif option == 3:
        print(ColorChalks.FCOLORS.Red + "You can delete binary file (to_do_list.dat) manually.")
    print(ColorChalks.COLORS.Reset)
to_do()
f.close()

    


