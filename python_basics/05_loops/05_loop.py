# Napisz program działający w nieskończonej pętli.

# Program pyta:

# Enter transaction amount or type exit:

# Zasady:

# użytkownik wpisuje exit → zakończ pętlę przez break,
# użytkownik wpisuje liczbę równą 0 lub ujemną → wyświetl Invalid transaction amount. i przejdź do następnego przebiegu przez continue,
# poprawna liczba → dodaj ją do daily_total i wyświetl aktualną sumę.

# Przykład:

# Enter transaction amount or type exit: 200
# Daily total: 200

# Enter transaction amount or type exit: -50
# Invalid transaction amount.

# Enter transaction amount or type exit: 300
# Daily total: 500

# Enter transaction amount or type exit: exit
# Transaction processing finished.

# Ponieważ input() zwraca str, najpierw sprawdź exit, a dopiero później konwertuj wartość na int.
daily_total = 0

while True:
    user_choice = input("Enter transaction amount or type exit: ")
    if user_choice == "exit":
        print("Transaction processing finished.")
        break
    transaction_amount = int(user_choice)
    if int(user_choice) <= 0:
        print("Invalid transaction amount.")
        continue

    daily_total += int(user_choice)
    print(f"Daily total: {daily_total}")
