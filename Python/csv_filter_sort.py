"""
csv_filter_sort.py
────────────────────────────────────────────────────────
Reads employee_sales_data.csv → filters rows with Sales > 20 000,
sorts them in descending order of Sales, and exports the result
to Excel as filtered_sorted_sales.xlsx.
"""


import pandas as pd

# Step 1: Load the file
df = pd.read_csv("employee_sales_data.csv")

# Step 2: Filter rows where Sales > 20,000
filtered = df[df["Sales"] >  20000]

# Step 3: Sort by Sales (descending)
filtered_sort = filtered.sort_values(by = "Sales", ascending = False)

# Step 4: Export to Excel
filtered_sort.to_excel("filtered_sorted_sales.xlsx", index= False)

# Step 5: Confirming successful file generation
print("Export complete: filtered_sorted_sales.xlsx")