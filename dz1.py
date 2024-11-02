import random

try:
    Days = int(input('How many days would you care for Гавчик: '))
except ValueError:
    print("Invalid input. Defaulting to 1 day.")
    Days = 1


class Human:
    def __init__(self, food):
        self.food = food

    def buy_food(self, dose):
        self.food += dose
        print(f"Bought {dose} units of food. Total food: {self.food}")

    def feed_pet(self, pet, dose):
        if self.food <= 0:
            print("No food left! Buying 10 units of food.")
            self.buy_food(10)

        if self.food >= dose:
            pet.feed(dose)
            self.food -= dose
            print(f"Fed {pet.name} {dose} units of food. Food left: {self.food}")
        else:
            print("Not enough food to feed the pet. Buying 10 units of food.")
            self.buy_food(10)


class Dog:
    def __init__(self, name):
        self.name = name
        self.happiness = 100
        self.energy = 100
        self.hunger = 0

    def feed(self, amount):
        self.hunger -= amount
        self.energy += amount + random.randint(1, 5)
        if self.hunger < 0:
            self.hunger = 0
        print(f"{self.name} has been fed. Hunger level: {self.hunger}")

    def play(self):
        if self.energy > 20:
            self.happiness += 10
            self.energy -= 20
            self.hunger += 5
            print(
                f"You played with {self.name}. Happiness: {self.happiness}, Energy: {self.energy}, Hunger: {self.hunger}")
        else:
            print(f"{self.name} is too tired to play.")

    def rest(self):
        self.energy += 30
        if self.energy > 100:
            self.energy = 100
        print(f"{self.name} is resting. Energy level: {self.energy}")

    def check_status(self):
        print(f"{self.name}'s Status: Happiness: {self.happiness}, Energy: {self.energy}, Hunger: {self.hunger}")

    def next_hour(self):
        self.hunger += random.randint(1, 5)
        self.happiness -= random.randint(0, 5)
        self.energy -= random.randint(0, 10)

        if self.happiness < 0:
            self.happiness = 0
        if self.hunger > 100:
            self.hunger = 100
        if self.energy < 0:
            self.energy = 0

        print(
            f"Hour passed. {self.name}'s Status: Happiness: {self.happiness}, Energy: {self.energy}, Hunger: {self.hunger}")


def simulate_days():
    gaw = Dog("Гавчик")
    owner = Human(food=20)

    days = Days
    for day in range(1, days + 1):
        print(f"\nDay {day} starts.")
        for hour in range(1, 17):
            gaw.next_hour()

            if gaw.happiness == 0 or gaw.energy == 0:
                print(f"{gaw.name} has suffered too much. Game over! You lost.")
                return

            action = input("What would you like to do? (feed/play/rest): ").strip().lower()
            if action == "feed":
                amount = int(input("How much food would you like to give? "))
                owner.feed_pet(gaw, amount)
            elif action == "play":
                gaw.play()
            elif action == "rest":
                gaw.rest()
            else:
                print("Invalid action. Please choose 'feed', 'play', or 'rest'.")

        print(f"Day {day} ends. Night begins.")

    print(f"Congratulations! You took care of {gaw.name} for {days} days and won!")


simulate_days()
