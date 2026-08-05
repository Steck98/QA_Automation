# Quest System

# Gracz chce odebrać nagrodę za misję.

# Nagroda może zostać odebrana tylko wtedy, gdy:

# misja jest ukończona,
# nagroda nie została jeszcze odebrana,
# gracz ma wolne miejsce w ekwipunku.

# Po odebraniu nagrody:

# ustaw informację, że nagroda została odebrana,
# zwiększ ilość złota o nagrodę,
# wypisz komunikat.

# Jeżeli nagrody nie da się odebrać, program ma podać wszystkie powody, dlaczego.

reward = 500
quest_completed = False
reward_redeemed = True
inventory_free_space = False
player_gold = 0


if quest_completed and inventory_free_space and not reward_redeemed:
    reward_redeemed = True
    player_gold += reward
    print("Reward Has been redeemed \nGold has been added to your account")
else:
    if reward_redeemed:
        print("Reward has beed arleady redeemed")
    if not quest_completed:
        print("The quest has not been completed yet")
    if not inventory_free_space:
        print("You don't have enough inventory space")
