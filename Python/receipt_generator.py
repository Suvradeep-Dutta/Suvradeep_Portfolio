name = input("Enter your name: ")
item = input("Item Purchased: ")
qty = int(input("Quantity Purchased: "))
price = int(input("Price per item: "))

print(f"\nHello {name}, \nThanks for Shopping with us!")
print(f"\nItem: {item} \nQuantity: {qty} \nTotal Bill: ₹{qty * price:.2f}")