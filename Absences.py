"""Takes a list of employee names and days absent so it can calculate the average"""


def get_name():
    name = ""
    absence_list = []
    while name != "$":
        name = input("Enter a name: ")
        if name == "$":
            if len(absence_list) > 0:
                end_program(absence_list)
                break
            else:
                print("No data was entered. Goodbye.")
                break

        days = int_check("Enter number of days absent: ")
        absence_list.append([name, days])


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


def end_program(absence_list):
    total = 0
    count = len(absence_list)
    most_absent = [["", 0]]
    not_absent = []
    for emp in absence_list:
        if emp[1] > most_absent[0][1]:
            most_absent[0] = emp
        elif emp[1] == most_absent[0][1]:
            most_absent.append(emp)
        elif emp[1] == 0:
            not_absent.append(emp)
        total += int(emp[1])
    calc_average(total, count, absence_list)
    calc_most_absent(most_absent)
    if len(not_absent) > 0:
        print("\nThe following employees were not absent this year: ")
        sorted_not_absent = sorted(not_absent)
        for emp in sorted_not_absent:
            print("\t", emp[0])
    else:
        print("\nThere were no employees who had 100% attendance this year.")
    print("\n********************************************************")


def calc_average(total, count, absence_list):
    average = round(total / count, 2)
    print(f"\n********************************************************"
          f"\nThe average days absent this year was {average}"
          f"\nEmployees who were absent above the average were: ")
    for emp in absence_list:
        if emp[1] > average:
            print(f"\t{emp[0]} who was absent for {emp[1]} days")


def calc_most_absent(most_absent):
    if len(most_absent) == 1:
        print(f"\nThe person most absent was {most_absent[0][0]} with"
              f"{most_absent[0][1]} days")
    else:
        print("\nThe people most absent this year were: ")
        for emp in most_absent:
            print(f"\t{emp[0]} with {emp[1]} days")


# Main
get_name()
