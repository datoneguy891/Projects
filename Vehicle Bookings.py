def int_checker(text_from_call):
    valid = False
    while not valid:
        try:
            number_to_check = int(input(text_from_call))
            if isinstance(number_to_check, int):
                valid = True
                return number_to_check

        except ValueError:
            print("This is invalid")


def booking():
    book_another = ""
    while book_another != "X":
        seats = int_checker("How many seats do you need?: ")
        print("These are the available vehicles: ")
        print("\tID", "\tTYPE OF VEHICLE")
        for vehicle in vehicle_pool:
            if vehicle[2] >= seats and vehicle[3]:
                print(f"\t{vehicle[0]}\t{vehicle[1]} seats: {vehicle[2]}")
        booked = int_checker("Enter the Car Number of the vehicle you would like to book ")
        name = input("What name do you want the booking under: ")
        history = vehicle_pool[booked - 1], name
        hired.append(history)
        vehicle_pool[booked - 1][3] = False
        print(f"You have booked ID {vehicle_pool[booked - 1][0]} "
              f"a {vehicle_pool[booked - 1][2]} "
              f"seater {vehicle_pool[booked - 1][1]}")

        print(f"Hired so far: {hired}")
        book_another = input("X to exit or any other key "
                             "to book another: ").upper()


vehicle_pool = [[1, "Suzuki Van", 2, True],
                [2, "Toyota Corolla", 4, True],
                [3, "Honda CRV", 4, True],
                [4, "Suzuki Swift", 4, True],
                [5, "Mitsubishi Airtrek", 4, True],
                [6, "Nissan DC Ute", 4, True],
                [7, "Toyota Previa", 7, True],
                [8, "Toyota Hi Ace", 12, True],
                [9, "Toyota Hi Ace", 12, True]]

hired = []

booking()
print("The vehicles hired today were: ")
for i in hired:
    print(f"\tID {i[0][0]} the {i[0][2]} seater {i[0][1]} hired by {i[1]}")
