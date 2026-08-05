# Gracz może wejść do lochu tylko wtedy, gdy spełnia wszystkie poniższe warunki:

# ma co najmniej 10 poziom,
# ma więcej niż 0 HP,
# ma co najmniej 100 sztuk złota.

player_health = int(input("How much hp you have left ? "))
player_level = int(input("What is your level? "))
player_gold = int(input("How much gold do you have? "))

if player_health > 0 and player_level >= 10 and player_gold >= 100:
    print("Access granted.")
else:
    print("Access denied.")
