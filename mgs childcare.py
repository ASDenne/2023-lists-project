def dropoff():
    Children.append(input("name?"))
    print("check in conformed")
def pickup():
    name = input("name")
    if name in Children:
        Children.remove(name)
    else:
        print("sorry they are not in our system currently")
def calcost():
    hours = int(input("time spent here"))
    print(f"${hours*len(Children)*12}.00")
def printroll():
    print(Children)
def main():
    task = input("do you want to pick up, drop off, or print roll")
    if task == "pick up":
        pickup()
    elif task == "drop off":
        dropoff()
    elif task == "print roll":
        printroll()
    if task == "X" or task == "":
        print("goodbye")
    else:
        main()
Children = []



main()
