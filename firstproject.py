menu = {
    'Pizza': 500,
    'Burger': 200,
    'Momo': 150,
    'Chowmine': 120,
    'Tea': 40
}

print("Welcome to my Restaurant")
print("Pizza: Rs.500")
print("Burger: Rs.200")
print("Momo: Rs.150")
print("Chowmine: Rs.120")
print("Tea: Rs.40")

order_total = 0

item1 = input("Enter the item you want to order: ").capitalize()

if item1 in menu:
    order_total += menu[item1]
    print(f"Your item {item1} has been placed and added to your order.")
else:
    print(f"Ordered item {item1} is not available currently.")

another_order = input("Do you want to order anything else? (Yes/No): ")

if another_order == "Yes":
    item2 = input("Enter another item you want to order: ").capitalize()

    if item2 in menu:
        order_total += menu[item2]
        print(f"Item {item2} has been added to your order.")
    else:
        print(f"Ordered item {item2} is currently not available.")

print(f"Your total money to pay is Rs.{order_total}")