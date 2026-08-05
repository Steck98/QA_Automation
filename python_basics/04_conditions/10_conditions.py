# Sklep sprzedaje trzy przedmioty:

# Item	            Price	Required Level

# Sword	            200	    5
# Armor	            500	    10
# Staff	            1500	20

# Gracz podaje:

# nazwę przedmiotu,
# swój poziom,
# ilość złota.

# Program ma:

# Sprawdzić, czy taki przedmiot istnieje.
# Jeżeli nie istnieje:
# Item not found.
# Jeżeli istnieje:
# sprawdzić poziom,
# sprawdzić złoto.
# Jeżeli wszystko się zgadza:
# odejmij złoto,
available_items = ["sword", "staff", "armor"]

player_gold = int(input("How much gold do you have? "))
player_level = int(input("What is your level? "))
selected_item = input(
    "What item would you like to buy ? \nI would reccomend a Sword, Armor or a Staff"
).lower()

if selected_item in available_items:
    if selected_item == "sword":
        item_level = 5
        item_price = 200
    elif selected_item == "staff":
        item_level = 20
        item_price = 1500
    else:
        item_level = 10
        item_price = 500

    if player_level >= item_level and player_gold >= item_price:
        player_gold -= item_price
        print(f"Congratulations you have a {selected_item}")
    else:
        if player_level < item_level and player_gold < item_price:
            print(
                f"You don't meet the required level and gold to buy this {selected_item}"
            )
        elif player_gold < item_price:
            print(f"You don't have enough gold to buy this {selected_item}")
        else:
            print(f"You don't meet the required level to buy this {selected_item}")

else:
    print("Your requested item does not exist or is not available in our store")
