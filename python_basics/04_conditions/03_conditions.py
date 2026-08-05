# Napisz program rozstrzygający jedną turę walki.

# Program pobiera:

# zdrowie gracza,
# zdrowie przeciwnika,
# obrażenia gracza,
# obrażenia przeciwnika,
# doświadczenie gracza,
# nagrodę XP za przeciwnika,
# złoto gracza,
# nagrodę w złocie.

# Kolejność walki
# Gracz atakuje pierwszy.

# Od zdrowia przeciwnika odejmowane są obrażenia gracza.

# Jeżeli przeciwnik zginął:
# nie może już zaatakować,
# gracz otrzymuje XP,
# gracz otrzymuje złoto,
# program wyświetla wynik walki i aktualne zasoby gracza.
# Jeżeli przeciwnik przeżył:
# atakuje gracza,
# od zdrowia gracza odejmowane są obrażenia przeciwnika.
# Następnie program wyświetla jeden z komunikatów:
# Enemy defeated.
# Player defeated.

# albo:

# Both characters are still alive.
# Wymagania

# Zdrowie po ataku nie powinno być wyświetlane jako liczba ujemna.

# Jeżeli przeciwnik zginie, gracz nie może otrzymać od niego obrażeń.

# XP i złoto są przyznawane wyłącznie po pokonaniu przeciwnika.

# Na końcu wyświetl czytelne podsumowanie

player_health = int(input("What is your health? "))
player_damage = int(input("What is your damage? "))
player_experience = int(input("What is your experience amount? "))
player_gold = int(input("How much gold do you have? "))

enemy_health = int(input("What is your enemy health? "))
enemy_damage = int(input("What is your enemy damage? "))
enemy_experience_reward = int(
    input("How much experience points you get for killing your enemy? ")
)
enemy_gold_reward = int(input("How much gold you receive for killing your enemy? "))

player_attack_result = enemy_health - player_damage
enemy_attack_result = player_health - enemy_damage
if player_attack_result <= 0:
    enemy_health = 0
    player_gold = player_gold + enemy_gold_reward
    player_experience = player_experience + enemy_experience_reward
    print("You won")
elif enemy_attack_result <= 0:
    enemy_health = player_attack_result
    player_health = 0
    print("Player Defeated")
else:
    player_health = enemy_attack_result
    enemy_health = player_attack_result
    print("Both characters are still alive")

print(
    f"Your Health: {player_health} \nYour Experience points: {player_experience} \nYour Gold: {player_gold}"
)
print(f"Enemy Health: {enemy_health} \nYour enemy damage: {enemy_damage}")
