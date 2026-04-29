import random

def game():
    food = 1500
    miles = 0
    bullets = 30
    money = 200
    day = 1

    party = [
        {"name": input("Name 1: "), "health": 100},
        {"name": input("Name 2: "), "health": 100}
    ]

    while miles < 500 and party:
        print("\nDay", day, "| Miles:", miles, "| Food:", food)

        for p in party:
            print(p["name"], p["health"])

        print("\n1 Travel  2 Rest  3 Hunt  4 Trade  5 Quit")
        c = input("> ")

        if c == "1":
            miles += random.randint(30, 60)
            food -= 30
            print("You traveled.")

            if random.randint(1, 3) == 1:
                p = random.choice(party)
                print(p["name"], "got sick!")
                p["health"] -= 20

        elif c == "2":
            food -= 15
            for p in party:
                p["health"] += 10
            print("You rested.")

        elif c == "3":
            if bullets >= 5:
                bullets -= 5
                gain = random.randint(80, 150)
                food += gain
                print("You got", gain, "food.")
            else:
                print("No bullets!")

        elif c == "4":
            amt = int(input("Money to spend on food: "))
            if amt <= money:
                food += amt * 10
                money -= amt

        elif c == "5":
            print("You quit the trail.")
            break

        # deaths
        for p in party[:]:
            if p["health"] <= 0:
                print(p["name"], "died.")
                party.remove(p)

        if food <= 0:
            for p in party:
                p["health"] -= 15

        day += 1

    if not party:
        print("\nEveryone died 💀")
    else:
        print("\nYou made it to Oregon! 🎉")


# MAIN MENU
while True:
    print("\n=== OREGON TRAIL ===")
    print("1. Start Game")
    print("2. Quit")

    choice = input("> ")

    if choice == "1":
        game()
    else:
        break