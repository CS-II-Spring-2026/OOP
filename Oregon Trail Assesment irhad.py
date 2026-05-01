#Oregon Trail Irhad 
#Making a character class
class Character:
    def __init__( self, name, job, health, food_supply, clothing, oxen, parts, cash):
        self.name = name
        self.job = job
        self.health = health
        self.food_supply = food_supply
        self.clothing = clothing
        self.oxen = oxen
        self.parts = parts
        self.cash = cash
        self.miles = 0

#Start Setup
Flag = True
Start_Game = False

while Flag:
    print("----Welcome To The Oregon Trail For Dummies!----")
    print("Start journey? : Press 1")
    print("What is the Oregon Trail? : Press 2")
    print("Quit : Press 9")

    selection = input("Enter your choice: ")

    if selection == "1":
        Start_Game = True
        print("Welcome!")
        Flag = False

    elif selection == "9":
        print("See ya")
        Flag = False

    elif selection == "2":
        print("The Oregon Trail was a long route"
        " (about 2,000 miles) used in the 1800s by pioneers traveling from the Midwest to the western United States, especially to Oregon.")
        Flag = True
#Main game loop
while Start_Game:
    name = input("What is your main characters name? ")
    print("Welcome", name)
    Start_Game = False

#Jobs
job = True

while job:
    print("Many made the trip to Oregon. You may:")
    print("1:Be a banker from Boston ")
    print("2:Be a carpenter from Ohio ")
    print("3:Be a farmer from Illinois ")
   
    job_input = input("What is your choice?")


    if job_input == "1":
        job = "Banker"
        cash = 800 
    elif job_input == "2":
        job = "Carpenter"
        cash = 500
    elif job_input == "3":
        job = "Farmer"
        cash = 500
    else:
        print("Sorry! Not an option. Click the enter key to pick again. ") , input(job)
    
    companions = int(input("How many companions? (Maximum of 4)"))
    print("You have", companions, " companions. ")
    job = False
#Character 

player = Character(name, job, 100, 0, 0, 0, 0, cash)
#shop
shop = True

while shop:
    print("You need supplies! Here you have a budget of $",cash , "pick out what you need!" )

    shop = False

shop = True

cattle_price = 50
clothes_price = 7.50
food_price = 10

while shop:
    print("\n--- General Store ---")
    print("Budget: $", player.cash)
    print("1. Buy oxen ($50 each)")
    print("2. Buy clothing ($7.50 per set)")
    print("3. Buy food ($10 per pound)")
    print("4. Leave shop")

    choice = input("What would you like to do? ")

    if choice == "1":
        amount = int(input("How many oxen would you like? "))
        cost = amount * cattle_price

        if cost <= player.cash:
            player.oxen += amount 
            player.cash -= cost
            print("You bought", amount, "oxen.")
        else: print("Not enough money!")

    elif choice == "2":
        amount = int(input("How many sets of clothing? "))
        cost = amount * clothes_price


        if cost <= player.cash:
            player.clothing += amount 
            player.cash -= amount
            print("You bought", amount, "sets of clothes.")
        else: print("Not enough money!")

    elif choice == "3":
        amount = int(input("How many pounds of food? "))
        cost = amount * food_price

        if cost <= player.cash:
            player.food_supply += amount
            player.cash -= cost
            print("You bought", amount, "pounds of food.")
        else:
            print("Not enough money!")

    elif choice == "4":
        print("Leaving the shop, see ya!")
        shop = False
    
    else:
        print("Invalid choice, try again.")
#Supplies list

print("\n--- Supplies Summary---")
print("Cattle:", player.oxen)
print("Clothes", player.clothing)
print("Food", player.food_supply)
print("Cash leftover: $", player.cash)

#Start journey
print("It's time to start our journey! Would you like to travel: ")
print("1: As fast as possible")
print("2: Steady")
print("3: Slow, very very slow ")
print("4: Enter a secret code... ")

pace_input = input("Make a choice! 1, 2, 3, or 4: ")

if pace_input in ["1", "2", "3"]:
    print("That didn't work out too well..... Sorry! Play again?")
elif pace_input == "4":
    code = input("Enter the secret code to win: ")
    
    if code == "Irhad is cool":
        print("You entered the correct code! A gypsy in his $100,000 BMW M4 Competition picked you up and drove you to Oregon! Btw Irhad is the coolest person on this planet")
    else:
        print("Wrong code you're dead, sucks to suck!")
else:
    print("Invalid choice. Please try again and choose 1-4.")
