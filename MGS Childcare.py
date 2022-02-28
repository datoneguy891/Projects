def main():
    choice = 0
    while choice != 5:
        print("------------------------------")
        print("Welcome to MGS Childcare\nWhat would you like to do? Please choose one of the items below")
        print("------------------------------")
        print()
        print("1 Drop Off a Child\n2 Pick up a Child\n3 Calculate Cost\n4 Print Roll\n5 Exit the system")
        print()
        choice = int(input("Enter your choice (Number between 1 and 5): "))
        print()

        if choice == 1:
            drop_child()

        if choice == 2:
            pick_child()

        if choice == 3:
            calccost()

        if choice == 4:
            print_roll()

        else:
            quit()


def drop_child():
    global number_of_children
    confirm_drop_off = input("This will cost $12 per hour. Are you certain? (Y/N): ").upper()
    if confirm_drop_off == 'Y':
        child_name = input("What is the name of your child?: ")
        child_list.append(child_name)
        number_of_children = + 1
        main()
    else:
        main()


def pick_child():
    global number_of_children
    confirm_pick_up = input("Are you certain? (Y/N): ").upper()
    if confirm_pick_up == "Y":
        child_remove = input("What is the name of the child you want to pick up?: ")
        child_list.remove(child_remove)
        number_of_children = - 1
    else:
        main()


def calccost():
    time_spent = int(input("How many hours will you leave your children for?: "))
    price = 12
    print(f"The cost for {time_spent} hours and {number_of_children} children is ${time_spent * price}")


def print_roll():
    print(child_list)


# main
child_list = []
number_of_children = 0
main()
