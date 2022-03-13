
'''
Brother Alex Bedino

assignmentweek10.py

Goal: create a working shopping cart
'''

shop_list = []
price_list = []

print("Welcome to the Shopping Cart Program!")
print()
while True:
    print ("Please select one of the following:")
    print ("1. Add item\n2. View cart\n3. Remove item\n4. Compute total\n5. Quit")
    choice = int(input("Please enter an action: ")) # starts the sequence
    while choice not in [1, 2, 3, 4, 5]: #added this while loop in case the user chooses a number out of range
        print("This is not a valid input, please try again")
        choice = int(input("Please enter an action: "))
    if choice == 1: # adding an item and price to the lists
        item = input("What item would you like to add?: ")
        price = float(input(f"What is the price of '{item}'?: "))
        shop_list.append(item)
        price_list.append(price)
        print (f"{item} has been added to the cart")
    elif choice == 2: # printing out the shopping list
        print("The contents of the shopping cart are:")
        for i in range(len(shop_list)):
            shop = shop_list[i]
            price = price_list[i]
            print(f"{i}. {shop} - ${price}")
        print()
    elif choice == 3: # removing item from the list
        change = int(input("Which item would you like to remove? "))
        shop_list.pop(change)
        price_list.pop(change)
    elif choice == 4: # compute subtotal
        print (f"The subtotal is ${sum(price_list)}")
    else:
        print (f"Goodbye, thank you!")
        break