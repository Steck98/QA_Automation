# Projektujesz system wejścia na arenę VIP.

# Gracz może wejść tylko wtedy, gdy:

# ma co najmniej 20 poziom,
# ma minimum 500 złota,
# nie jest zbanowany.

# Jeżeli wszystkie warunki są spełnione:

# Welcome to the VIP Arena!

# W przeciwnym razie program ma podać konkretny powód odmowy.

player_level = int(input("What is your level? "))
player_gold = int(input("How much gold do you have?"))
is_player_banned = False

if player_gold >= 500 and player_level >= 20 and not is_player_banned:
    print("Access granted.")
else:
    if is_player_banned:
        print("Access denied. Your are banned")
    if player_level < 20:
        print("Access denied. Your Level is too low")
    if player_gold < 500:
        print("Access denied. Not enought gold")
