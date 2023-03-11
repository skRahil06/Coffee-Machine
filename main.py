menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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

condition = True
total_money=0
water_remaining=resources['water']
milk_remaining=resources['milk']
coffee_remaining=resources['coffee']

while condition:

    coffee = input("What would you like? (espresso/latte/cappuccino):")

    if coffee=="latte" or coffee=="cappuccino" or coffee=="espresso" or coffee=="report" or coffee=="off":
        available = "false"
        if coffee == "espresso":
            if menu["espresso"]["ingredients"]["water"] > water_remaining:
                print("“Sorry there is not enough water.")
            elif menu["espresso"]["ingredients"]["coffee"] > coffee_remaining:
                print("“Sorry there is not enough coffee.")
            else:
                available = "true"

        elif coffee == "latte":
            if menu["latte"]["ingredients"]["water"] > water_remaining:
                print("“Sorry there is not enough water.")
            elif menu["latte"]["ingredients"]["milk"] > milk_remaining:
                print("“Sorry there is not enough milk.")
            elif menu["latte"]["ingredients"]["coffee"] > coffee_remaining:
                print("“Sorry there is not enough coffee.")
            else:
                available = "true"
        elif coffee == "cappuccino":
            if menu["cappuccino"]["ingredients"]["water"] > water_remaining:
                print("“Sorry there is not enough water.")
            elif menu["cappuccino"]["ingredients"]["milk"] > milk_remaining:
                print("“Sorry there is not enough milk.")
            elif menu["cappuccino"]["ingredients"]["coffee"] > coffee_remaining:
                print("“Sorry there is not enough coffee.")
            else:
                available = "true"
        elif coffee == "report":
            print(f"water: {water_remaining}")
            print(f"milk: {resources['milk']}")
            print(f"coffee: {resources['coffee']}")
            print(f"money: ${total_money}")

        elif coffee == "off":
            quit()

        else:
            print("invalid")

        if available == "true":
            print("please insert coins.")
            quarters = int(input("how many quarters?:"))
            dimes = int(input("how many dimes?:"))
            nickles = int(input("how many nickles?:"))
            pennies = int(input("how many pennies?:"))

            paid_money = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
            if coffee == "report":
                pass
            elif paid_money >= menu[coffee]["cost"]:
                return_money = round((paid_money - menu[coffee]["cost"]), 2)
                print(f"Here is ${return_money} dollars in change.")
                print(f"Here is your {coffee}. Enjoy!”. ")
                total_money += menu[coffee]["cost"]
                water_remaining -= menu[coffee]["ingredients"]["water"]
                milk_remaining -= menu[coffee]["ingredients"]["milk"]
                coffee_remaining -= menu[coffee]["ingredients"]["coffee"]
            elif coffee == "latte" or coffee == "cappuccino" or coffee == "espresso" or paid_money < menu[coffee][
                "cost"]:
                print("Sorry that's not enough money. Money refunded.")
            else:
                print("invalid")


    else:
        print("invalid")


