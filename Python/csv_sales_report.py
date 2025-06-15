import csv

filename = "sales_data.csv"
total_bill = 0

print("===== SALES REPORT =====\n")

with open(filename, newline='') as file:
    reader = csv.DictReader(file)

    for row in reader:
        item = row["Item"]
        qty = int(row["Units"])
        price_per_unit = int(row["Price"])
        gst = float(row["GST (%)"])
        discount = float(row["Discount (%)"])

        base_price = qty * price_per_unit
        gst_amt = base_price * (gst / 100)
        discount_amt = base_price * (discount / 100)
        final_price = (base_price + gst_amt) - discount_amt

        total_bill += final_price

        print(f"{item} | Qty: {qty} | ₹{final_price:.2f}")

print(f"\nTotal Revenue: ₹{total_bill:.2f}")
