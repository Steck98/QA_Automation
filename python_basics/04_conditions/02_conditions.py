# Player level
# Player health
# Required level
# Entry fee
# Player gold

player_level = int(input("What is your level?"))
player_health = int(input("What is your health?"))
required_level = int(input("What is the required level to enter the dungeon?"))
dungeon_entry_fee = int(input("What is the dungeon entry price?"))
player_gold = int(input("How much gold you have?"))

if player_level < required_level:
    print("Access denied: level too low.")
elif player_health <= 0:
    print("Access denied: character is dead.")
elif dungeon_entry_fee > player_gold:
    print("Access denied: not enough gold.")

else:
    print(f"Access granted. Gold remaining: {player_gold - dungeon_entry_fee}")
