# Napisz funkcję:

# calculate_salary(hours_worked, hourly_rate)

# Ma zwrócić wynagrodzenie.

# Jeżeli pracownik przepracował:

# do 160 godzin → normalna stawka,
# powyżej 160 godzin → każda dodatkowa godzina jest płatna 150% stawki.


def payroll(net_worth, working_time):

    print(calculate_salary(net_worth, working_time))


def calculate_salary(hour_wage, work_hours):
    if work_hours > 160:
        return (work_hours % 160) * (hour_wage / 100 * 50 + hour_wage) + (
            hour_wage * 160
        )

    return hour_wage * work_hours


payroll(50, 180)
