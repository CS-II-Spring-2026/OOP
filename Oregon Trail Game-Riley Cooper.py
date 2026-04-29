#Oregon Trail Game-Riley Cooper
import random
def CharInfo ():
    print("Hunter: Specializes in hunting for food.")
    print("Banker: Starts with more money.")
    print("Guide: Has more health and can guide the party.")

#Parent Class
class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.hunger = 0
        self.money = 1000
        self.food = 60
        self.alive = True

#Child Class

class Hunter(Player):
    def __init__(self, name):
        super().__init__(name)
        self.food = 80

    def hunt(self):
        self.food += 20
        print(f"You went hunting and found some food! You now have {self.food} food.")
    
class Banker(Player):
    def __init__(self, name):
        super().__init__(name)
        self.money = 1200

class Guide(Player):
    def __init__(self, name):
        super().__init__(name)
        self.health = 120  

    def guide(self):
        print("You used your guiding skills to navigate the trail more efficiently, speed increased by 15%")

#Main Menu
flag = True
while flag == True:
    print("----Oregon Trail Menu----")
    print("1. Create a new Character")
    print("2. Read the story")
    print("3. Goal of the game")
    print("4. Quit")
    selection = input("Make a selection: ")
    if selection == "1":
        print("Let's create your character!")
        name = input("What is your name? ")
        char = False
        while char == False:
            print("Choose your character class:")
            print("1. Hunter")
            print("2. Banker")
            print("3. Guide")
            print("4. More information about classes")
            class_selection = input("Make a selection: ")
            #Checks what class the player is
            if class_selection == "1":
                player1 = Hunter(name)
                char = True
            elif class_selection == "2":
                player1 = Banker(name)
                char = True
            elif class_selection == "3":
                player1 = Guide(name)
                char = True
            elif class_selection == "4":
                CharInfo()

        print(f"Welcome {player1.name}, you are a {type(player1).__name__} and ready to start your adventure!")

        #Game Menu Loop
        flag2 = True
        while flag2 == True:
            print("----Game Menu----")
            print("1. Actions")
            print("2. Check status")
            print("3. Continue on the trail")
            print("4. Quit")
            selection2 = input("Make a selection: ")
            #Actions that the player can do
            if selection2 == "1":
                print("----What would you like to do?----")
                print("1. Hunt for food")
                print("2. Ask for help from a guide")
                print("3. Rest to regain health")
                print("4. Repair your wagon")
                print("5. Return to the main menu")
                action_selection = input("Make a selection: ")
                if action_selection == "1" and isinstance(player1, Hunter):
                    #Hunt to gain food
                    player1.hunt()
                elif action_selection == "2" and isinstance(player1, Guide):
                    #Guide has you navigate the trail more quickly
                    player1.guide()
                elif action_selection == "3":
                    #Rest to regain health
                    player1.health += 20
                    print(f"You rested and gained health! Your health is now {player1.health}.")
                elif action_selection == "4":
                    #Fix the Wagon
                    print("You repaired your wagon and can now continue on the trail!")
                elif action_selection == "5":
                    print("Back to Game Menu")
                    break





            elif selection2 == "2":
                print(f"Health: {player1.health}, Hunger: {player1.hunger}, Money: {player1.money}, Food: {player1.food}")
            elif selection2 == "3":
                print("You continue on the trail, facing new challenges and adventures!")
                miles_traveled = + 5
                event = random.randint(1, 8)
                #Random events that can happen on the trail
                if event == 1:
                    print("\nA bear attacks! You lose 20 health.")
                    player1.health -= 20
                elif event == 2:
                    print("\nCholera spreads through camp. You lose 30 health.")
                    player1.health -= 30
                elif event == 3:
                    print("\nYou find wild berries. You gain 10 food.")
                    player1.food += 10
                elif event == 4:
                    print("\nRough travel uses up supplies. You lose 15 food.")
                    player1.food -= 15
                elif event == 5:
                    print("\nYou find a river crossing. You lose 10 health.")
                    player1.health -= 10
                elif event == 6:
                    print("\nYou find a trading post and you can buy supplies.")
                    buy_supplies = input("Press Y to buy supplies for $50 and gain 20 food. Press N to skip: ")
                    if buy_supplies == "Y" or buy_supplies == "y":
                        player1.money -= 50
                        player1.food += 20
                        print(f"You have {player1.money} money and {player1.food} food.")
                    else:
                        print("You decided not to buy supplies.")
                elif event == 7:
                    print("\nYou encounter friendly natives who share food. You gain 15 food.")
                    player1.food += 15
                elif event == 8:
                    print("\nYou get caught in a storm and lose supplies. You lose 20 food and 15 health.")
                    player1.food -= 20
                    player1.health -= 15
                #Show the results of traveling
                print(f"You have traveled {miles_traveled} miles.")
                print(f"Current status - Health: {player1.health}, Hunger: {player1.hunger}, Money: {player1.money}, Food: {player1.food}")
            elif selection2 == "4":
                print("Thanks for playing! Goodbye!")
                flag2 = False
            else:
                print("Invalid selection. Please choose a number from the menu.")
    #Main Menu Options Continued
    elif selection == "2":
        print("The Oregon Trail was a roughly 2,000-mile, 4-6 month overland route used by over 400,000 settlers, farmers,\nand adventurers in the mid-19th century to reach the Pacific Northwest, specifically Oregon's Willamette Valley, from Missouri.\nStarting in the 1840s, pioneers braved disease, dangerous river crossings, and mountainous terrain, driven by promises of free land and a better life,\nmaking it a defining, treacherous saga of American westward expansion.")
    elif selection == "3":
        print("The goal of the game is to successfully make it across The Oregon Trail with your family/crew while managing your resources and making strategic decisions along the way.\n" "You will need to hunt for food, manage your health, and make choices that will affect your journey.")
    elif selection == "4":
        print("Thanks for playing! Goodbye!")
        flag = False
    else:
        print("Invalid selection. Please choose a number from the menu.")


