import pandas as pd

# Step 1: Load the excel file.
df= pd.read_excel("monthly_sales_data.xlsx")

# Step 2: Clean the data.
df_clean = df.dropna(subset=["Units Sold", "Unit Price"])
df_clean["Date"] = pd.to_datetime(df_clean["Date"])
df_clean = df_clean.reset_index(drop= True)

# Step 3: Add new columns.
df_clean["Month"] = df_clean["Date"].dt.strftime("%b")
df_clean["Sales"] = df_clean["Units Sold"] *  df_clean["Unit Price"]

# Step 4: Grouping and Summarizing.
sales_by_product = df_clean.groupby("Product")["Sales"].sum().reset_index()
sales_by_month = df_clean.groupby("Month")["Sales"].sum().reset_index()
sales_by_region = df_clean.groupby("Region")["Sales"].sum().reset_index()

# Step 5: Writing all data into one single workbook
with pd.ExcelWriter("monthly_sales_report.xlsx", engine="xlsxwriter") as writer:
    df_clean.to_excel(writer, sheet_name= "Cleaned Data", index= False)
    sales_by_product.to_excel(writer, sheet_name="Sales by Product", index= False)
    sales_by_month.to_excel(writer, " Sales by Month", index= False)
    sales_by_region.to_excel(writer, "Sales by Region", index= False)

# Step 6: Confirming successful report generation.
print("Monthly sales report generated successfully!")