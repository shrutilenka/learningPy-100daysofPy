auction_bids = {}


def bid(name, amt):
    auction_bids[name] = amt


def result():
    '''This function determines the winner of the auction based on the highest bid.'''
    # above line is called docstring useful for documentation, tesea rae nt comment    max_bid = 0
    winner = ""
    for i in auction_bids:
        if auction_bids[i] > max_bid:
            max_bid = auction_bids[i]
            winner = i
    print(f"The winner is {winner} with a bid of ${max_bid}")


def main():
    while True:
        name = input("Enter your name: ")
        amt = int(input("Enter your bid: $"))
        bid(name, amt)
        end = input("Has the bid ended? (yes/no): ")
        if end.lower() == "yes":
            result()
            break


main()
