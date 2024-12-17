'''#Define the  menu of Restaurant
menu = {
    "Pizza":40,
    "Pasta":50,
    "Burger":60,
    "Salad": 70,
    "Coffee":80,
}
#Greet
print("Welcome to the Python Restaurant")
print("Pizza :Rs40\nPasta:Rs50\nBurger:Rs60\nSalad:Rs70\nCoffee:Rs80")


order_total =0
item_1 = input("Enter the name of item you want to order =")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item {item_1} has been added to your order")

else:
    print("Please order something else")             
    
    
another_item = input("Do you want to add another item?(Yes/No)")
if another_item == "N":
    print(f"Your bill is {order_total}")
elif another_item =="Yes":
    item_2 = input("Please enter the name of the second item =")
    if item_2 in menu:
        order_total +=menu[item_2]
    else:
        print(f"Not available {item_2}")
    print(f"The total amount to pay is {order_total}")'''
    
    # Define the menu of the Restaurant
menu = {
    "Pizza": 40,
    "Pasta": 50,
    "Burger": 60,
    "Salad": 70,
    "Coffee": 80,
}

# Greet the customer and display the menu
print("Welcome to the Python Restaurant!")
print("Menu:")
for item, price in menu.items():
    print(f"{item}: Rs{price}")

order_total = 0

# Loop to take multiple orders
while True:
    item = input("Enter the name of the item you want to order: ")
    if item in menu:
        order_total += menu[item]
        print(f"{item} has been added to your order.")
    else:
        print(f"{item} is not available. Please choose something else.")

    # Ask if they want to add another item
    another_item = input("Do you want to add another item? (Yes/No): ").strip().lower()
    if another_item == "no":
        break

# Display the total bill
print(f"Your total bill is: Rs{order_total}")
