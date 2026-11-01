print("===welcome to holiday activity planner===")
print("step 1: pick your holiday type:")
print("1- beach type")
print("2- mountain type")
print("select any one:")
choice = int(input("enter 1 or 2:"))
if choice == 1:
    print("step 2: pick your beach activity")
    print("1- swimming")
    print("2- sandcastle building")
    print("select any one:")
    beach_activity = int(input("enter 1 or 2:"))
    if beach_activity == 1:
        print("you picked : swimming")
        print("best time : morning")
        print("remember :  carry sunscreen and water")
    else:
        print("you picked : sandcastle building")
        print("best time : evening")
        print("remember : carry a bucket and toy showel ")
elif choice == 2:
    print("pick your mountain activity:")
    print("1- camping")
    print("2- hiking")
    mountain_activity = int(input("enter 1 or 2:"))
    if mountain_activity == 1:
        print("you picked : camping ")
        print("best for : staying close to nature")
        print("remember : carry a tent and flashlight")
    else:
        print("you picked : hiking")
        print("best for : exploring trails")
        print("remember : wear comfortable shoes")
else:
    print("that was not a valid choice.")
    print("please enter 1 for beach holiday or 2 for mountain holiday")
print("===your holiday plan is ready===")
print("===enjoy your trip===")
