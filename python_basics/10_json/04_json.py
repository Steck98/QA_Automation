import json


def run_ticket_proccess():
    with open("python_basics/10_json/tickets.json") as file:
        data = json.load(file)
        display_ticket(data)
        if not display_ticket(data):
            print("Ticket not found.")


def display_ticket(ticket_list):
    searched_ticket = input(
        "What are the last 4 digits of the ticket you are looking for? "
    )

    for ticket in ticket_list:
        if ticket["id"] == f"TCK-{searched_ticket}":
            print(f"Ticket ID: {ticket['id']}")
            print(f"Status: {ticket['status']}")
            print(f"Priority: {ticket['priority']}")
            print(f"Customer: {ticket['customer']['name']}")
            print(f"Customer e-mail: {ticket['customer']['email']}")
            print(f"Company name: {ticket['customer']['company']['name']}")
            print(f"Company location: {ticket['customer']['company']['city']}")
            print("\nMessages")
            for message in ticket["messages"]:
                print(f"\nauthor: {message['author']}\nContent: {message['content']}")
            modify_ticket = input(
                "Would you like to modify anything in this ticket? yes/no"
            )
            if modify_ticket == "yes":
                update_ticket(ticket, ticket_list)
            return True
    return False


def update_ticket(ticket, ticket_list):
    ticket_update_value = int(
        input(
            "Which value would you like to modify? \n1.ID\n2.Status\n3.Priority\n4.Customer"
        )
    )
    if ticket_update_value != 4:
        for i, key in enumerate(ticket):
            if i + 1 == ticket_update_value:
                ticket.update({key: input(f"What is the new {key}? ")})
                with open("python_basics/10_json/tickets.json", "w") as file:
                    json.dump(ticket_list, file, indent=4)
                    break
    elif ticket_update_value == 4:
        customer_update_value = int(
            input("Which value would you like to modify? \n1.name\n2.email\n3.company")
        )
        if customer_update_value == 1 or customer_update_value == 2:
            for i, key in enumerate(ticket["customer"]):
                if i + 1 == customer_update_value:
                    ticket["customer"].update(
                        {key: input(f"What is the new customer {key}? ")}
                    )
                    with open("python_basics/10_json/tickets.json", "w") as file:
                        json.dump(ticket_list, file, indent=4)
                        break
        elif customer_update_value == 3:
            company_update_value = int(
                input("What company info would you like to modify? \n1.name\n2.city")
            )
            for i, key in enumerate(ticket["customer"]["company"]):
                if i + 1 == company_update_value:
                    ticket["customer"]["company"].update(
                        {key: input(f"What is the new company {key}? ")}
                    )
                    with open("python_basics/10_json/tickets.json", "w") as file:
                        json.dump(ticket_list, file, indent=4)
                        break
        else:
            print("Wrong Value")
    else:
        print("wrong value")


run_ticket_proccess()
