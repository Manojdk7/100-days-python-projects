def find_highest_bid(bids):
    winner=""
    highest_bid=0
    for bidder in bids:
        bid_amount=bids[bidder]
        if bid_amount>highest_bid:
            highest_bid=bid_amount
            winner=bidder
   

    print(f"The winner is {winner} with a bid of ${highest_bid}")

bid={}
continue_bidding=True
while continue_bidding: 
    name=input("What is your name?: ")
    price=int(input("What is your bid?: $"))
    bid[name]=price
    should_continue=input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if should_continue=="no":
        continue_bidding=False
        find_highest_bid(bid)
    elif should_continue=="yes":
        print("\n" * 50)
