def refill_input_checker():
    refill_value = input()

    while True:
        if refill_value.isnumeric():  # isnumeric() used as it returns False if number is negative
            return int(refill_value)
        else:
            refill_value = input('Error: input must be numeric, please try again\n')


def coffee_machine():
    # MACHINE SETTINGS
    # initial quantities of ingredients (and cash) stored in machine
    storage = {'ml of water': 400,
               'ml of milk': 540,
               'grams of coffee beans': 120,
               'disposable cups': 9,
               'of money': 550}

    # the recipes for each type of coffee and price
    espresso_recipe = {'ml of water': 250,
                       'ml of milk': 0,
                       'grams of coffee beans': 16,
                       'disposable cups': 1,
                       'of money': -4}  # price is a negative value so that it will add to cash value when 'deducted'

    latte_recipe = {'ml of water': 350,
                    'ml of milk': 75,
                    'grams of coffee beans': 20,
                    'disposable cups': 1,
                    'of money': -7}

    cappuccino_recipe = {'ml of water': 200,
                         'ml of milk': 100,
                         'grams of coffee beans': 12,
                         'disposable cups': 1,
                         'of money': -6}

    # what types of coffee the machine can produce
    coffee_options = {'1': espresso_recipe,
                      '2': latte_recipe,
                      '3': cappuccino_recipe}

    # MACHINE FUNCTIONS
    while True:  # while machine is switched on
        action = input("Write action (buy, fill, take, remaining, exit): ")
        print()

        if action == 'buy':
            selection = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: ")

            if selection == 'back':
                print()
                continue
            elif selection in coffee_options.keys():
                # checking sufficient resources are available for selection
                out_of_resource = 0

                for each in coffee_options[selection]:
                    if each == 'of money':
                        pass  # do nothing
                    elif coffee_options[selection][each] > storage[each]:
                        print(f"Sorry not enough {each.replace('ml of ', '').replace('grams of ', '')}!")
                        out_of_resource = 1
                # reducing the existing storage by values specified in the coffees' recipe
                # increasing cash storage by price of coffee specified in the coffees' recipe
                if out_of_resource == 0:
                    for each in coffee_options[selection]:
                        storage[each] -= coffee_options[selection][each]
                    print('I have enough resources, making you a coffee!')

            else:
                print("Error: option is unavailable")

            print()

        elif action == 'fill':  # increase ingredients and cash stored in machine
            for each in storage:
                if each != 'of money':  # machine does not use a cash float
                    print(f"Write how many {each} you want to add: ")
                    storage[each] += refill_input_checker()
            print()

        elif action == 'take':
            print(f"I gave you ${storage['of money']}")
            storage['of money'] = 0
            print()

        elif action == 'remaining':
            print("The coffee machine has:")
            for each in storage:
                # if statement is special case handler for cash values
                print(f"{'$' if each == 'of money' else ''}{storage[each]} {each}")
            print()

        elif action == 'exit':
            exit()

        else:
            print('Error: option unavailable\n')


if __name__ == '__main__':
    coffee_machine()
