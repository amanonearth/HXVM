from rating import *
def choicepy():
    vmnum = input("[+] How many Virtual Machines do you want to run on your system? ")
    vmnumint = int(vmnum)
    print("\n")
    print(" 1. Kali Linux\n 2. Windows 10\n 3. Ubuntu\n 4. Parrot OS\n") # Options & beautification
    # choice = ['Kali Linux', 'Windows 10', 'Ubuntu', 'Parrot OS']
    # print(choice)

    print(f"Please select any " + vmnum + " options:")

    for i in range(0, vmnumint):
        if i == 0:
            opt1 = int(input("Option 1: "))
        if i == 1:
            opt2 = input("Option 2: ")
        if i == 2:
            opt3 = input("Option 3: ")
        if i == 3:
            opt4 = input("Option 4: ")
        if i == 4:
            opt5 = input("Option 5: ")



    if vmnumint <= rating:
        print(f"You Can run " + vmnum + " Virtual Machine without any problem!!")

    else:
        print(f"\nYour machine is not capable of running " + vmnum + " Virtual Machines!\n")
        print(f"Recommendation: You can run " + ratingstr + " Virtual Machine(s) without any problem!!\n")