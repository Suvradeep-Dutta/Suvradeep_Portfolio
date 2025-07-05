import pandas as pd

# Step 1: Load the file
df= pd.read_csv("employee_project_data.csv")

# Step 2: Remove rows with missing employee or salary info
df_clean= df.dropna(subset=["Employee_Name", "Department", "Project", "Salary"])
df_clean["Salary"]= pd.to_numeric(df_clean["Salary"], errors='coerce')
df_clean= df_clean.dropna(subset=["Salary"]).reset_index(drop= True)

# Step 3: Add Calculations -> Median Salary per department
median_salary_per_department= df_clean.groupby("Department")["Salary"].median().reset_index()

# Step 4: Writing all data into one single  excel workbook
with pd.ExcelWriter("employee_median_salary.xlsx", engine= "xlsxwriter") as writer:
    median_salary_per_department.to_excel(writer, sheet_name= "Median Salary per Department", index= False)

# Step 5: Confirming successful report generation.
print("Excel report generated successfully!")