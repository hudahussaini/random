import os


def get_item_price_and_quantity(item_name, item_dict):
    shcok = item_dict.get(item_name)
    if item_name in item_dict:
        price = item_dict[item_name][0]
        quantity = item_dict[item_name][1]
        #why doesnt this work -> quantity = item_dict.get(item_name)
        return price, quantity


def change_item_dict(item_name, item_dict, price, quantity):
   # Change existing dictionary entry or create a new one with given values
    item_dict[item_name][0] = price
    item_dict[item_name][1] = quantity
    print(f'{item_name} is updated')

def add_item(item_name, item_dict):
    if item_name not in item_dict:
        price = float(input("Please enter the item price "))
        quantity = int(input("Please enter the quantity of the item "))
        item_dict.update({item_name : [price, quantity]})
        return item_dict
    else:
        print("That item is already for sale, please update it instead")


def update_item(item_name, item_dict):
    if item_name in item_dict:
        price, quantity = get_item_price_and_quantity(item_name, item_dict)
        print(f"{item_name} costs: ${price:.2f} and there are {quantity} available")

        price = float(input("Please enter the new item price "))
        quantity = int(input("Please enter the new quantity of the item "))

        item_dict[f'{item_name}'][0] = price
        item_dict[f'{item_name}'][1] = quantity
        print(f"Now {item_name} costs: ${price:.2f} and there are {quantity} available")
        return item_dict
    else:
        print("That item is not for sale currently, please add it")


def remove_item(item_name, item_dict):
    if item_name in item_dict:
        print("Before -> ", item_dict)
        del item_dict[item_name]
        print( f"This {item_name} has been removed -> ", item_dict)
        return item_dict
    else:
        print("That item is not for sale currently")

def main():
    item_dict = {}

    program_on = 'y'

    while program_on == 'y':
            
        mode = input("Do you want to Shop or Manage? or quit ").lower()

        if mode == 'quit':
            exit()

        elif mode == 'shop':

            # shop mode from https://github.com/EricCharnesky/CIS2131-Summer2022/blob/main/Week7/main.py
            continue_buying = 'y'

            while continue_buying == 'y':
                item = input("Welcome to our amazing vending machine, what do you want to buy? ")
                if item in item_dict:
                    price, quantity_available = get_item_price_and_quantity(item, item_dict)

                    print(f"{item} costs: ${price:.2f} and there are {quantity_available} available ")

                    quantity_to_buy = quantity_available + 1

                    while quantity_to_buy > quantity_available:
                        quantity_to_buy = int(input(f"How many {item} do you want to buy? "))

                    print(f"That will cost ${quantity_to_buy * price}")

                    change_item_dict(item, item_dict, price, (quantity_available - quantity_to_buy))

                    print("Thanks for shopping with us, come again, Thanks!")

                else:
                    print("sorry we don't sell that")

                continue_buying = input("Do you want to buy more? y/n ")

        elif mode == 'manage':

            continue_managing = 'y'

            while continue_managing == 'y':

                choice = input("Do you want to Add an item, Update an item, or Remove an item? ").lower()
                item_name = input("What is the item name you want to manage? ")
                if choice == "add":
                    add_item(item_name, item_dict)
                elif choice == "update":
                    update_item(item_name, item_dict)
                elif choice == "remove":
                    remove_item(item_name, item_dict)
                else:
                    print("I can't help with that")

                continue_managing = input("Do you want to manage more? y/n ")
    
    program_on = input(" Do you want to continue, y/n ")


main()