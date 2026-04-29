#Jakub Novak
import random

class Character:
    def __init__(self, name):
        self.name = name
        self.health = 100

    def show_stats(self):
        print(f"{self.name} | Health: {self.health}")


def start_game():
    print("=== THE OREGON TRAIL ===")
    print("1. Start Game")
    print("2. Quit")

    answer = input("Choose an option ")
    return answer
#Enter your name and choose your character
def setup_player():
    print("\n--- Create Your Party ---")
    name = input("Enter your name: ")

    print("\nChoose your profession:")
    print("1. Banker")
    print("2. Farmer")
    print("3. Carpenter")

    choice = input("Enter choice: ")
# You have 3 choices
    if choice == "1":
        money = 900
        food = 100
    elif choice == "2":
        money = 250
        food = 750
    else:
        money = 500
        food = 500

    cows = 0
    clothes = 0

    player = Character(name)

    print(f"\nWelcome, {name}!")
    return player, money, food, cows, clothes

#Here is your shop, You need to buy stuff
def shop(money, food, cows, clothes):
    print("\n--- Welcome to the Shop ---")
    while True:
        print(f"\nMoney: ${money}")
        print("1. Food ($0.5)")
        print("2. Cows ($30)")
        print("3. Clothes ($8)")
        print("4. Leave")

        choice = input("Choose: ")

        if choice == "1":
            amt = int(input("How many pounds of food do you want to buy? "))
            print(f"You bought {amt} pounds of food")
            cost = amt * .5
            if cost <= money:
                food += amt
                money -= cost
           

        elif choice == "2":
            amt = int(input("How many cows do you want to buy? "))
            print(f"You bought {amt} cows")
            cost = amt * 30
            if cost <= money:
                cows += amt
                money -= cost

        elif choice == "3":
            amt = int(input("How many clother do you want to buy? "))
            print(f"You bought {amt} clothes")
            cost = amt * 8
            if cost <= money:
                clothes += amt
                money -= cost

        elif choice == "4":
            break

    return money, food, cows, clothes

# Start of the game
def play_game(player, money, food, cows, clothes):
    distance = 0
    goal = 1000

    print("\n--- THE JOURNEY STARTS ---")

    while distance < goal and food > 0:
        print(f"\nDistance: {distance}/{goal}")
        print(f"Food: {food}")
#Choose what do you want to do
        print("\n1. Travel")
        print("2. Rest")
        print("3. Hunt")
        print("4. Shop")
        print("5. Trade")
        print("6. Look Around")

        choice = input("Choose: ")

        if choice == "1":
            miles = random.randint(50, 120)
            distance += miles
            food = random.randint(30,90)
            print(f"You traveled {miles} miles.")

        elif choice == "2":
            food -= 5
            print("You rested.")

        elif choice == "3":
            gain = random.randint(10, 40)
            food += gain
            print(f"You hunted and gained {gain} food.")
        elif choice == "4":
            money, food, cows, clothes = shop(money, food, cows, clothes)
            print("You finished shopping.")
        elif choice == "5":
            print("\n--- Trade ---")
            print("You trade with a traveler...")

            trade_type = random.choice(["food", "money"])

            if trade_type == "food":
                gain = random.randint(5, 20)
                food += gain
                print(f"You received {gain} food in a trade.")
            else:
                gain = random.randint(5, 25)
                money += gain
                print(f"You received ${gain} in a trade.")
        elif choice == "6":
            print("\n--- Looking Around ---")

            event = random.choice([
                "You see a peaceful valley ahead.",
                "You spot smoke in the distance.",
                "Nothing but empty land for miles.",
                "You find abandoned supplies!"
            ])

            print(event)

            if "supplies" in event:
                bonus = random.randint(5, 15)
                food += bonus
                print(f"You gained {bonus} food!")

        event = random.random()
        if event < 0.2:
            print("Bad weather! You lose food.")
            food -= 10
        elif event < 0.25:
            print("Someone got sick!")
            food -= 15
#If you reached the goal then you're in Earlham 
        if distance >= 1000:
            print(f"You did it, you reached Earlham. You traveled {distance} miles.")
if start_game():
    player, money, food, cows, clothes = setup_player()
    play_game(player, money, food, cows, clothes)
else:
    print("Goodbye!")