import pandas as pd

# Step 1: Load the file
df = pd.read_csv("employee_project_data.csv")

# Step 2: Remove rows with missing employee or salary info
df_clean = df.dropna(subset=["Employee_Name", "Department", "Project", "Slary"])
df_clean["Salary"] = pd.to_numeric(df_clean["Salary"], errors = 'coerce' )
df_clean = df_clean.dropna(subset = ["Salary"]).reset_index(drop= True)

# Step 3: Add Calculations
# A: Total salary per department
salary_by_department = df_clean.groupby("Department")["Salary"].sum().reset_index()

# B: Average salary per project
salary_per_project = df_clean.groupby("Project")["Salary"].mean().reset_index()

# C: Employee count per department
employee_per_department = df_clean.groupby("Department")["Employee_Name"].nunique().reset_index(name= "Employee_Count")

#  D: Top 3 earners
top_earners = df_clean.sort_values(by= "Salary", ascending= False).head(3)

# E: Employees on more than 2 project
project_count = df_clean.groupby("Employee_Name")["Project"].nunique().reset_index(name="Project_Count")
multi_proj_emp = project_count[project_count["Project_Count"] > 2]

# Step 4: Writing all data into one single  excel workbook
with pd.ExcelWriter("employee_summary_report.xlsx", engine="xlsxwriter") as writer:
    df_clean.to_excel(writer, sheet_name="Cleaned Data", index= False)
    salary_by_department.to_excel(writer, sheet_name="Salary By Department", index= False)
    salary_per_project.to_excel(writer, sheet_name= "Salary By Project", index= False)
    employee_per_department.to_excel(writer, sheet_name= "Employees Per Department", index= False)
    top_earners.to_excel(writer, sheet_name= "Top 3 Earners", index= False)
    multi_proj_emp.to_excel(writer, sheet_name= "Multi-Project Employees", index= False)

# Step 5: Confirming successful report generation.
print("Excel report generated successfully!")