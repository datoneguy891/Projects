"""A program that lets you bid in a silent auction
Jamie Yang, Finished 4/3/22"""


def main():
    print("By continuing, you accept that you will be participating in a silent auction.")
    continuing = input("Do you want to continue? (Y/N): ").upper()
    if continuing == "Y":
        global item_sold
        item_sold = input("What is the auction for?: ")
        global reserve_price
        reserve_price = int(input("What is the reserve price?: "))
        print(f"The auction for the {item_sold} is starting.\nYou can finish bidding by typing -1.")
        start_auction()


def start_auction():
    bid = int(input("What is your bid?: "))
    bids_so_far.append(bid)
    print(f"The highest bid so far is ${max(bids_so_far)}")
    if bid == -1:
        print(f"The auction for the {item_sold} finished with a bid of {max(bids_so_far)}. The reserve price was"
              f" {reserve_price}")
        quit()
    elif bid < max(bids_so_far):
        print("Please enter a higher bid.")
        start_auction()
    else:
        start_auction()


# main
bids_so_far = []
main()
"""Please send help I have no idea how to stop the auction"""
