import pandas as pd

# Step 1: Load the file
df= pd.read_csv("attendance_data.csv")

# Step 2: Clean and prepare the data
df_clean = df.dropna(subset=["Date", "Employee", "Status"])
df_clean["Date"]= pd.to_datetime(df_clean["Date"])
df_clean =  df_clean.reset_index(drop=True)

# Step 3: Add Month column
df_clean["Month"]= df_clean["Date"].dt.strftime("%b")

# Step 4: Total number of days attended per employee
attendance_count = df_clean[df_clean["Status"] == "Present"].groupby("Employee")["Date"].count().reset_index(name= "Days Present")

# Step 5: Total number days each employee attended in each month
monthly_attendance = df_clean.groupby(["Employee", "Month"]).size().reset_index(name= "Days Present")

# Step 6: Employees with full attendance
total_days = df_clean["Date"].nunique()
full_attendance = attendance_count[attendance_count["Days Present"] == total_days]

# Step 7: Days absent per employee
absences = df_clean[df_clean["Status"] == "Absent"].groupby("Employee")["Date"].count().reset_index(name= "Days Absent")

# Step 8: Employees with the most absences
top_absentees = absences.sort_values(by= "Days Absent", ascending= False).head(3)

# Step 9: Consolidating data into separate sheets within a single Excel workbook
with pd. ExcelWriter("attendance_report.xlsx", engine= 'xlsxwriter') as writer:
    df_clean.to_excel(writer, sheet_name= "Cleaned Data", index= False)
    attendance_count.to_excel(writer, sheet_name= "Attendance Count", index= False)
    monthly_attendance.to_excel(writer, sheet_name= "Monthly Tend", index= False)
    full_attendance.to_excel(writer, sheet_name= "Full Attendance", index= False)
    absences.to_excel(writer, sheet_name= "Days Absent", index= False)
    top_absentees.to_excel(writer, sheet_name= "Top Absentees", index= False)

# Step 10: Confirming successful report generation
print("Attendance Report generated successfully!")
