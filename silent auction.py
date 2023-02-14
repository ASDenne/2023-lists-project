object = input("what is the auction for?")
min_price = float(input("what is the reserve price?"))
print()
print(f"the auction for the {object} has started")
bid = 0
highest_bid = 0
while bid != -1:
    print(f"highest bid so far is ${highest_bid}")
    bid = float(input("what is your bid"))
    if bid > highest_bid*1.01:#so you don't go up by cents when dealing with big items
        highest_bid = bid
    else:
        print("please enter a higher bid")
print()
if highest_bid > min_price:
    print(f"the auction for {object} finished with a bid of ${highest_bid}")
else:
    print("no bids greater then the reserve price entered"
          "no items sold")
