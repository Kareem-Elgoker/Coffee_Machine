class CoffeeMachine:
    def __init__(self, water, milk, coffee_beans, cups, money):
        self.water = water
        self.milk = milk
        self.coffee_beans = coffee_beans
        self.cups = cups
        self.money = money

    def __str__(self):
        return f"""The coffee machine has:
{self.water} of water
{self.milk} of milk
{self.coffee_beans} of coffee beans
{self.cups} of disposable cups
${self.money} of money"""

    def buy(self, num):
        quantity = {
            1: [250, 0, 16, 4],
            2: [350, 75, 20, 7],
            3: [200, 100, 12, 6]
        }.get(num, None)

        not_enough = list(self.enough(quantity))

        if not not_enough:
            print("I have enough resources, making you a coffee!")
            self.water -= quantity[0]
            self.milk -= quantity[1]
            self.coffee_beans -= quantity[2]
            self.money += quantity[3]
            self.cups -= 1

        else:
            things = ", ".join(not_enough)
            print(f"Sorry, not enough {things}!")

    def fill(self, water, milk, coffee, cups):
        self.water += water
        self.milk += milk
        self.coffee_beans += coffee
        self.cups += cups

    def take(self):
        print(f"I gave you ${self.money}")
        self.money = 0

    def enough(self, lst):
        if self.water - lst[0] < 0:
            yield "water"
        if self.milk - lst[1] < 0:
            yield "milk"
        if self.coffee_beans - lst[2] < 0:
            yield "coffee beans"


obj1 = CoffeeMachine(400, 540, 120, 9, 550)

while True:
    action = input(
        "Write action (buy, fill, take, remaining, exit):\n").lower().strip()

    if action == "exit":

        break

    elif action == "remaining":

        print(obj1)

    elif action == "buy":

        num = input(
            "What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n").strip()
        if num == "back":
            continue
        else:
            obj1.buy(int(num))

    elif action == "fill":

        water_n = int(
            input("Write how many ml of water do you want to add:\n").strip())
        milk_n = int(
            input("Write how many ml of milk do you want to add:\n").strip())
        coffee_beans_n = int(
            input("Write how many grams of coffee beans do you want to add:\n").strip())
        cups_n = int(
            input("Write how many disposable cups of coffee do you want to add:\n").strip())
        obj1.fill(water_n, milk_n, coffee_beans_n, cups_n)

    elif action == "take":

        obj1.take()
