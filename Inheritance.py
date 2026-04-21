# Oregon Trail OOP Example
# Demonstrates: Inheritance, super(), and unique class attributes


# Parent Class

class Character:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.health = 100  # shared by all characters

    def show_stats(self):
        print(f"{self.name} | Age: {self.age} | Health: {self.health}")



# Child Classes


class Soldier(Character):
    def __init__(self, name, age):
        super().__init__(name, age)  # inherit from Character
        self.strength = 10

    def attack(self):
        print(f"{self.name} attacks with strength {self.strength}!")


class Banker(Character):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.money = 1000

    def spend_money(self, amount):
        self.money -= amount
        print(f"{self.name} now has ${self.money}")


class Fisherman(Character):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.food = 50

    def fish(self):
        self.food += 10
        print(f"{self.name} caught fish! Food: {self.food}")



# Main Program

# Create characters
player1 = Soldier("John", 30)
player2 = Banker("Alice", 40)
player3 = Fisherman("Sam", 25)

print("\n--- Character Stats ---")
player1.show_stats()
player2.show_stats()
player3.show_stats()

print("\n--- Actions ---")
player1.attack()
player2.spend_money(200)
player3.fish()

# Simple Game Loop (Optional Extension)


print("\n--- Simple Turn ---")
players = [player1, player2, player3]

for player in players:
    if isinstance(player, Soldier):
        player.attack()
    elif isinstance(player, Banker):
        player.spend_money(50)
    elif isinstance(player, Fisherman):
        player.fish()