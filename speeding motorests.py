criminals = ["james wilson", "helga norman", "zachary conroy"]
activity = []
speed_fines = [[0,30],[10,80],[15,120],[20,170],[25,230],[30,300],[35,400],[40,510],[45,630]]
total_fine = 0
while input("end of day (Y/N").upper() != "Y":
    name = input("name of speeder").lower()
    if criminals.__contains__(name) == True:
        print(f"{name} has a warrent to arrest")
    speed = int(input("how far over the speed limit"))
    fine = 0
    for n in range(1,len(speed_fines)):
        if speed >= speed_fines[n][0]:
            fine = speed_fines[n][1]
    print(f"{name} owes ${fine}")
    total_fine += fine
    activity.append([name,speed,fine])
print(f"total fines {len(activity)}")
for n in range(0,len(activity)):
    print(f"{activity[n][0]} went {activity[n][1]} over the speed limit and receaved a ${activity[n][2]} dollar fine")
print(f"total fines of {total_fine}")
