import pandas as pd

# Step 1: Load the file
df = pd.read_csv("inventory_data.csv")

# Step 2: Clean the data
df_clean = df.dropna(subset=["Item Name", "Stock", "Price"])
df_clean["Stock"]= pd.to_numeric(df_clean["Stock"], errors= 'coerce')
df_clean["Price"]= pd.to_numeric(df_clean["Price"], errors= 'coerce')
df_clean= df_clean.dropna(subset= ["Stock", "Price"]).reset_index(drop= True)

# Step 3: Add calculated columns
df_clean["Stock Value"] = df_clean["Stock"] * df_clean["Price"]
reorder_threshold = 10
df_low_stock = df_clean[df_clean["Stock"] < reorder_threshold]

# Step 4: Export to Excel with multiple sheets
with pd.ExcelWriter("inventory_report.xlsx", engine= "xlsxwriter") as writer:
    df_clean.to_excel(writer, sheet_name= "Full Inventory", index= False)
    df_low_stock.to_excel(writer, sheet_name= "Low Stock Items", index= False)

# Step 5: Confirming successful report generation
print("Inventory report generated successfully!")