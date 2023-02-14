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
    task = input("do you want to pick up(u), drop off(d), or print roll(r) calc cost(c)")
    if task == "pick up" or task == "u":
        pickup()
    elif task == "drop off" or task == "d":
        dropoff()
    elif task == "print roll" or task == "r":
        printroll()
    elif task == "calc cost" or task == "c":
        calcost()
    if task == "X" or task == "":
        print("goodbye")
    else:
        main()
Children = []



main()
