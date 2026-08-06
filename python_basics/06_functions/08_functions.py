# Firma ma następujące zasady.

# Pracownik może złożyć wniosek o urlop tylko wtedy, gdy:

# ma minimum 1 rok stażu,
# ma przynajmniej 1 dzień urlopu,
# nie jest obecnie na zwolnieniu lekarskim.

# Program ma pobrać:

# lata pracy,
# liczbę dni urlopu,
# czy pracownik jest na L4 (yes/no).

# Jeżeli wszystkie warunki są spełnione:

# Vacation approved.

# W przeciwnym razie wypisz konkretny powód odmowy.

# Przykłady:

# Vacation denied.
# Reason: employee is on sick leave.

# albo

# Vacation denied.
# Reason: no vacation days remaining.

# Jeżeli powodów jest kilka, wypisz wszystkie.
def vacation_calculator():
    worked_years = int(input("Since how many years are you working at our company? "))
    free_days = int(input("How many free days you have left? "))
    sick_leave = input("Are you on a sick leave? yes/no ").lower()

    if vacation_validator(worked_years, free_days, sick_leave):
        print("Vacation approved.")


def vacation_validator(worked_years, free_days, sick_leave):
    if worked_years < 1:
        print("Vacation denied. \nReason: your lengh of servie is not enought")
    if free_days < 1:
        print("Vacation denied. \nReason: no vacation days remaining")
    if sick_leave == "yes":
        print("Vacation denied. \nReason: employee is on sick leave")
    return worked_years >= 1 and free_days >= 1 and sick_leave == "no"


vacation_calculator()
