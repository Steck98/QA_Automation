user_name = input("What is your name ? ")
user_last_name = input("What is your last name ? ")
print(f"Welcome {user_name} {user_last_name}")

killed_monsters = input("How many monster did u killed ? ")
print(f"You have killed {killed_monsters} monsters.")

gold_amount = int(input("How much gold do you have?"))
gold_earned = int(input("How much gold did you earn?"))
total_gold = gold_earned + gold_amount
print(f"You now have {total_gold} gold.")
