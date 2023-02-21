def avaliable(seats):
    for n in range(0 ,len(cars_avalible)):
        if cars_avalible[n][3] == "":
            extra = ""
            if seats > cars_avalible[n][2]:
                extra = "which isn't enougth seats for you"
            print(f"option {cars_avalible[n][0]} is the {cars_avalible[n][1]} which seats {cars_avalible[n][2]} {extra}")
        else:
            print(f"option {cars_avalible[n][0]} the {cars_avalible[n][1]} has been booked by {cars_avalible[n][3]}")
cars_avalible = [[1,"Suzuki Van",2,""],[2,"toyota corolla",4,""],[3,"honda crv",4,""],[4,"suzuki",4,""],[5,"mitisibishi",4,""],[6,"nissan dc ute",4,""],[7,"toyota previa",7,""],[8,"toyota Hi Ace",12,""],[9,"toyota hi ace",12,""]]
seats = 0
cars_booked = 0
while input("finished?(Y/N)").lower() != "y" and cars_booked < len(cars_avalible):
    name = input("who is booking the car?")
    seats = int(input("how many seats?"))
    if seats == -1:
        break
    avaliable(seats)
    vehicle = int(input("which vehicle do you want (enter option number)"))
    if cars_avalible[vehicle-1][3] != "":
        print(f"option {cars_avalible[vehicle-1][0]} the {cars_avalible[vehicle-1][1]} is currently booked out by {cars_avalible[vehicle-1][3]}")
    elif cars_avalible[vehicle-1][2] < seats:
        print(f"option {cars_avalible[vehicle-1][0]} the {cars_avalible[vehicle-1][1]} has only {cars_avalible[vehicle-1][2]} seats")
        if input("do you still want to book it(y/n)").lower() == "y":
            cars_booked += 1
            cars_avalible[vehicle-1][3] = name
    else:
        cars_avalible[vehicle-1][3] = name
        cars_booked += 1
        print(f" you have booked the {cars_avalible[vehicle-1][1]} under the name {cars_avalible[vehicle-1][3]}")
avaliable(0)
