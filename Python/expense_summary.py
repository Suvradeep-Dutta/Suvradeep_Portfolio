"""
expense_tracker.py
────────────────────────────────────────────────────────
Reads expense_data.csv → cleans → builds:

  • Monthly totals  (YYYY‑MM)
  • Category totals (Food, Rent, etc.)
  • Pivot table     (Month × Category)

Exports all sheets to expense_report.xlsx
"""


import pandas as pd

# Step 1: Load the file
df = pd.read_csv("expense_data.csv")

# Step 2: Clean and prepare the data
df["Date"]= pd.to_datetime(df["Date"])
df["Amount"]= pd.to_numeric(df["Amount"], errors='coerce')
df= df.dropna(subset=["Amount", "Category"]).reset_index(drop=True)

# Step 3: Add Year‑Month column
df["YearMonth"] = df["Date"].dt.to_period("M").astype('str')

# Step 4: Calculating Monthly Total
monthly_total = df.groupby("YearMonth")["Amount"].sum().reset_index(name = "Total Amount").sort_values("YearMonth")

# Step 5: Calculating overall total amount per category
category_total = df.groupby("Category")["Amount"].sum().reset_index(name= "Total Amount").sort_values("Total Amount", ascending= False)

# Step 6: Reshaping data to show monthly total amount for each category
pivot_month_cat = pd.pivot_table(df, values= "Amount", index= "YearMonth", columns= "Category", aggfunc= "sum", fill_value= 0).reset_index()

# Step 7: Consolidating data into separate sheets within a single Excel workbook
with pd.ExcelWriter("expense_report.xlsx", engine= 'xlsxwriter') as writer:
    df.to_excel(writer, sheet_name= "Cleaned Data", index= False)
    monthly_total.to_excel(writer, sheet_name= "Monthly_Totals", index = False)
    category_total.to_excel(writer, sheet_name= "Category_Totals", index= False)
    pivot_month_cat.to_excel(writer, sheet_name= "Pivot_Month_Category", index= False)

# Step 8: Confirming successful report generation.
print("Excel report generated successfully!")
