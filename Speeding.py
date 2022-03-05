def main():
    name = ""
    total_value = 0
    fine_list = []
    while name != "X":
        print("\n##################")
        name = input("Enter the name of the speeder: ").title()
        if name == "X":
            print_summary(total_value, fine_list)
            break
        else:
            check_warrant(name)
            amount_over = int_check("Enter the amount over the speed limit: ")
            fine = int(calc_fine(amount_over))
            total_value += fine
            if fine > 0:
                fine_list.append([name, amount_over])
            print(f"{name} to be fined ${fine}")


def print_summary(total_fines, fine_list):
    print(f"\n\n****** SUMMARY ******\n\n"
          f"Total fines: {len(fine_list)}")
    for fine in fine_list:
        print(f"{fine_list.index(fine) + 1}) "
              f"Name: {fine[0]}\tAmount Over Limit: {fine[1]}")
    print(f"Total amount of fines: ${total_fines}")


def calc_fine(amount_over):
    if amount_over > 0:
        if amount_over < 10:
            fine = 30
        elif amount_over < 15:
            fine = 80
        elif amount_over < 20:
            fine = 120
        elif amount_over < 25:
            fine = 170
        elif amount_over < 30:
            fine = 230
        elif amount_over < 35:
            fine = 300
        elif amount_over < 40:
            fine = 400
        elif amount_over < 45:
            fine = 510
        else:
            fine = 630
        return fine
    else:
        return 0


def int_check(text):
    valid = False
    while not valid:
        try:
            number_to_check = int(input(text))
            if isinstance(number_to_check, int):
                valid = True
                return number_to_check
        except ValueError:
            print("This is invalid")


def check_warrant(name):
    warrant_list = ["James Wilson", "Helga Norman", "Zachary Conroy"]
    if name in warrant_list:
        print(f"{name} - warrant to arrest".upper())


# Main
print("************ Speeding motorists - fines calculator ************\n"
      "enter 'X' for the name to exit the program and produce a summary")

main()
