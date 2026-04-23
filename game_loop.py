import random
def random_event(player):
    event = random.randint(1, 4)

    if event == 1:
        print("\nA bear attacks!")
        player.take_damage(20)

    elif event == 2:
        print("\nCholera spreads through camp!")
        player.take_damage(30)

    elif event == 3:
        print("\nYou find wild berries.")
        player.gain_food(10)

    elif event == 4:
        print("\nRough travel uses up supplies.")
        player.lose_food(15)

player = Soldier("John", 30)

turn = 1

while player.is_alive() and turn <= 5:
    print(f"\n--- Turn {turn} ---")
    player.show_stats()

    choice = input("Choose an action: rest, hunt, special: ").lower()

    if choice == "rest":
        player.health += 10
        if player.health > 100:
            player.health = 100
        print(f"{player.name} rests and recovers health.")

    elif choice == "hunt":
        player.gain_food(10)

    elif choice == "special":
        player.special_action()

    else:
        print("Invalid choice. You lose your turn.")

    random_event(player)

    turn += 1

if player.is_alive():
    print("\nYou survived the journey!")
else:
    print("\nGame over.")