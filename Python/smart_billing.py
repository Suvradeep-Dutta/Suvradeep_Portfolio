def billing_system(qty, price, GST, discount):
    base_price = qty * price
    discount_amt = base_price * (discount / 100)
    GST_amt = base_price * (GST / 100)
    final_price = base_price + GST_amt - discount_amt
    return final_price

def final_bill(items, total_amount):
    print("\n===== FINAL BILL =====")
    print("Total number of items purchased:", len(items))
    
    for i in items:
        print(i["Item"], "-", i["Quantity"], "-", i["Price"], "-",
              i["Discount (%)"], "-", i["GST (%)"], "-", f"₹{i['Final_Price']:.2f}")
        
    print("----------------------------")
    print("Total Bill Amount: ₹{:.2f}".format(total_amount))


# 🧾 Main Program
print("***** SMART BILLING SYSTEM *****")
mylist = []
Total_Bill = 0

n = int(input("Enter number of items: "))

for i in range(n):
    item = input("Item Name: ")
    qty = int(input("Quantity: "))
    price = int(input("Price: "))
    discount = float(input("Discount Offered (in %): "))
    GST = float(input("GST Applied (in %): "))
    
    Final_Price = billing_system(qty, price, GST, discount)
    Total_Bill += Final_Price

    mydict = {
        "Item": item,
        "Quantity": qty,
        "Price": price,
        "Discount (%)": discount,
        "GST (%)": GST,
        "Final_Price": Final_Price
    }

    mylist.append(mydict)

final_bill(mylist, Total_Bill)