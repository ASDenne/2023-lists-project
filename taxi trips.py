trips = 0
Tprofit = 0
Ttime = 0
name = input("what is your name?")
counitue = input("except new ride")
while counitue != "no" and counitue != "n":
    time = int(input("length of trip"))
    profit = time*2 + 10
    Tprofit += profit
    Ttime += time
    print(f"a trip of {time} minutes costs {profit} bring total profit to {Tprofit}")
    trips += 1
    counitue = input("except new ride")
print(f"good job {name}"
      f"in {Ttime} you made a profit of {Tprofit}"
      f"each rid took on average speed {Ttime/trips} minutes "
      f"and an average of ${Tprofit/trips} profit per trip")
