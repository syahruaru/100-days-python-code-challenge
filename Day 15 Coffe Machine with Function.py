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
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def is_sufficient(order_ingredients):
    for key in order_ingredients:
        if resources[key] < order_ingredients[key]:
            print(f"Sorry there are not enough {key}")
            return False
    return True

def process_coin():
    print("Please Insert Coin.")

    quarters = int(input("how many quarters?:"))
    dimes = int(input("how many dimes?:"))
    nickles = int(input("how many nikcles?:"))
    pennies = int(input("how many pennies?:"))
    total = quarters*0.25 + dimes*0.1 + nickles*0.05 + pennies*0.01
    return total

def payment_process(payment,drink_cost):
    '''return true when coin enough'''
    global profit
    if payment > drink_cost:
        change = round(payment - drink_cost,2)
        print(f"Here is your change ${change}")
        profit += drink_cost
        return True
    elif payment == drink_cost:
        profit += drink_cost
        return True
    else:
        print("Sorry not enough money, your money is refunded")
        return False

def make_order(resources_ingredients,order_ingredients):
    for key in order_ingredients:
        resources_ingredients[key]-= order_ingredients[key]




is_on = True
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ".lower())
    print(choice)

    if choice == 'off':
        print("The Machine is off, Thank You")
        is_on = False
    elif choice == 'report':
        for key in resources:
            print(f"{key}: {resources[key]}")
        print(f"Profit: {profit}")
    elif choice != 'espresso' and choice != 'latte' and choice != 'cappuccino':
        print("Please Typing Correctly")
    else:
        drink = MENU[choice]
        if is_sufficient(drink['ingredients']):
            total_coin = process_coin()
            print(total_coin)
            if payment_process(total_coin ,drink['cost']):
                make_order(resources,drink['ingredients'])
                print(f"This is Your Order: {choice}, Thank You!")


