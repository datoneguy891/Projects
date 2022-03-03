"""A program that lets you find the amount and time from a taxi service
Jamie Yang, Finished 4/3/22"""


def main():
    print("Thank you for choosing our Taxi service.")
    global driver_name
    driver_name = input("What is your driver's name?: ")
    choice = input("Would you like to start a trip? (Y/N): ").upper()
    if choice == "Y":
        record_trips()
    else:
        print_records()


def record_trips():
    time_spent = int(input("How long in minutes did the trip take?: "))
    total_time_spent.append(time_spent)
    price_of_time = 10 + time_spent * 2
    print(f"Your cost comes to {price_of_time}")
    prices.append(price_of_time)
    redo = input("Would you like to go on another trip? (Y/N): ").upper()
    if redo == "Y":
        record_trips()
    else:
        print_records()


def print_records():
    print(f"Your driver's name was {driver_name}")
    print("Your total time was ", sum(total_time_spent))
    print("Your average time was ", sum(total_time_spent) / len(total_time_spent))
    print("Your total income was ", sum(prices))
    print("Your average income was ", sum(prices) / len(prices))


# Main
prices = []
total_time_spent = []
main()
