# Założenie: dołączasz do zespołu jako junior QA Automation
# Python developer. Dostajesz fragment systemu, którego wcześniej nie widziałeś.
# Nie masz dokumentacji i musisz najpierw zrozumieć kod.#

# Za co odpowiada każda funkcja.
# Jak wygląda pełna droga programu od run_accounting_system().
# Co dokładnie dzieje się po wybraniu opcji "1".
# Co dzieje się przy przetwarzaniu miesięcznej paczki faktur.
# Po co program zapisuje:
# previous_balance = company_balance
# Jak system rozpoznaje, czy faktura została przetworzona, czy odrzucona.
# Kiedy wykonuje się continue.
# Kiedy wykonuje się break.
# Dlaczego process_invoice() zwraca stare saldo przy błędzie.
# Co oznacza:
# invoice_number[3:]
# Jakie wartości zwracają poszczególne funkcje.
# Co stanie się dla:
# salda firmy: 50000,
# numeru faktury: FV-1234567,
# kwoty netto: 1000,
# VAT: 23,
# faktury nieopłaconej.
# Znajdź minimum trzy potencjalne problemy lub słabe decyzje projektowe.
# Podaj minimum pięć przypadków testowych, które sprawdziłbyś jako QA.
# Jedna rzecz jest celowo lekko ukryta: kod zawiera rozwiązania,
# które działają, ale niekoniecznie są najlepszym sposobem projektowania systemu księgowego.
# Twoim zadaniem jest nie tylko opisać kod, ale też zakwestionować jego założenia.


def validate_invoice_number(invoice_number):
    if len(invoice_number) != 10:
        return False

    if not invoice_number.startswith("FV-"):
        return False

    for character in invoice_number[3:]:
        if not character.isdigit():
            return False

    return True


def calculate_vat(net_amount, vat_rate):
    return net_amount * vat_rate / 100


def calculate_gross_amount(net_amount, vat_rate):
    vat_amount = calculate_vat(net_amount, vat_rate)
    return net_amount + vat_amount


def can_process_invoice(net_amount, vat_rate, is_paid):
    valid_vat_rates = [0, 5, 8, 23]

    return net_amount > 0 and vat_rate in valid_vat_rates and not is_paid


def process_invoice(company_balance):
    invoice_number = input("Enter invoice number: ")

    if not validate_invoice_number(invoice_number):
        print("Invoice rejected: invalid invoice number.")
        return company_balance

    net_amount = float(input("Enter net amount: "))
    vat_rate = int(input("Enter VAT rate: "))
    payment_status = input("Has the invoice already been paid? yes/no: ").lower()

    is_paid = payment_status == "yes"

    if not can_process_invoice(net_amount, vat_rate, is_paid):
        print("Invoice rejected.")

        if net_amount <= 0:
            print("Reason: invalid net amount.")

        if vat_rate not in [0, 5, 8, 23]:
            print("Reason: unsupported VAT rate.")

        if is_paid:
            print("Reason: invoice has already been paid.")

        return company_balance

    gross_amount = calculate_gross_amount(net_amount, vat_rate)

    if gross_amount > company_balance:
        print("Invoice rejected: insufficient company funds.")
        return company_balance

    company_balance -= gross_amount

    print("Invoice processed successfully.")
    print(f"Net amount: {net_amount}")
    print(f"VAT rate: {vat_rate}%")
    print(f"Gross amount: {gross_amount}")
    print(f"Remaining company balance: {company_balance}")

    return company_balance


def run_accounting_system():
    company_balance = 50000
    processed_invoices = 0
    rejected_invoices = 0

    while True:
        print("\n===== ACCOUNTING SYSTEM =====")
        print("1. Process one invoice")
        print("2. Process monthly invoice batch")
        print("3. Show accounting summary")
        print("4. Close accounting period")

        user_choice = input("Choose an option: ")

        if user_choice == "1":
            previous_balance = company_balance
            company_balance = process_invoice(company_balance)

            if company_balance < previous_balance:
                processed_invoices += 1
            else:
                rejected_invoices += 1

        elif user_choice == "2":
            invoice_count = int(input("How many invoices are in the batch? "))

            if invoice_count <= 0:
                print("Invalid invoice count.")
                continue

            for invoice_index in range(1, invoice_count + 1):
                print(f"\nProcessing invoice #{invoice_index}")

                previous_balance = company_balance
                company_balance = process_invoice(company_balance)

                if company_balance == previous_balance:
                    rejected_invoices += 1
                    continue

                processed_invoices += 1

                if company_balance <= 1000:
                    print("Warning: company balance is critically low.")
                    break

        elif user_choice == "3":
            print("\n===== ACCOUNTING SUMMARY =====")
            print(f"Processed invoices: {processed_invoices}")
            print(f"Rejected invoices: {rejected_invoices}")
            print(f"Current company balance: {company_balance}")

        elif user_choice == "4":
            print("Accounting period closed.")
            break

        else:
            print("Invalid option.")

    print("\n===== FINAL REPORT =====")
    print(f"Processed invoices: {processed_invoices}")
    print(f"Rejected invoices: {rejected_invoices}")
    print(f"Final company balance: {company_balance}")


run_accounting_system()
