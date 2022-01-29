MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


# TODO 2: Ask user for coins
# TODO 3: Convert user's input into dollars
def taking_money_from_user():
    quarters = float(input("How many quarters? "))
    dimes = float(input("How many dimes? "))
    nickles = float(input("How many nickels? "))
    pennies = float(input("How many pennies? "))
    return 0.25 * quarters + 0.1 * dimes + 0.05 * nickles + 0.01 * pennies


# TODO 6: If beverage is dispensed update resources
def resources_calculator():
    required_water = MENU[user_choice]["ingredients"]["water"]
    required_coffee = MENU[user_choice]["ingredients"]["coffee"]

    if user_choice != "espresso":
        required_milk = MENU[user_choice]["ingredients"]["milk"]
        resources["milk"] = resources["milk"] - required_milk

    resources["water"] = resources["water"] - required_water
    resources["coffee"] = resources["coffee"] - required_coffee
    return resources


# TODO 1: Ask the user for his choice of beverage
# TODO 2: Verify the user amount

valid_inputs = ['latte', 'espresso', 'cappuccino', 'off', 'report']
is_resource_sufficient = True
user_payment = 0

while is_resource_sufficient:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if user_choice not in valid_inputs:
        print("This is an invalid input, please try again !!")

    elif user_choice == "off":
        is_resource_sufficient = False

    elif user_choice == "report":
        resources["money"] = user_payment
        print(f'Water: {resources["water"]}ml \n'
              f'Milk: {resources["milk"]}ml \n'
              f'Coffee: {resources["coffee"]}g \n'
              f'Money:$ {resources["money"]}')

    else:
        cost_of_drink = MENU[user_choice]["cost"]
        required_water = MENU[user_choice]["ingredients"]["water"]
        if required_water > resources["water"]:
            print("Sorry there is not enough water.")
        else:
            print("Please insert coins.")
            user_payment = taking_money_from_user()
            user_payment = round(user_payment,2)
            if user_payment >= cost_of_drink:
                remaining_change = user_payment - cost_of_drink
                rounded_remaining_change = round(remaining_change,2)
                print(f"Here is ${rounded_remaining_change} in change.")
                print(f"Here is your {user_choice} ☕️. Enjoy!")
                resources = resources_calculator()
            else:
                print("Sorry that's not enough money. Money refunded.")