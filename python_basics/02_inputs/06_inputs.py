# Mini projekt — Character Creator

# Tworzysz kreator postaci do gry RPG.

# Program ma zapytać użytkownika o:

# Character name
# Character class
# Character race
# Character level
# Current HP
# Maximum HP
# Gold

character_name = input("What is your name?")
character_class = input("What is your class?")
character_race = input("What is your race?")
character_level = int(input("What is your level?"))
character_current_health = int(input("What is your actual health?"))
character_maximum_health = int(input("What is your maximum health?"))
character_gold = float(input("What is your gold amount?"))

print(f"Name: {character_name}")
print(f"Class: {character_class}")
print(f"Race: {character_race}")

print(f"Level: {character_level}")

print(f"Health: {character_current_health}/{character_maximum_health}")

print(f"Gold: {character_gold}")
