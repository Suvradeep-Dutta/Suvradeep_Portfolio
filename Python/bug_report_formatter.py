filename= input("Enter name for the bug file you want to create(without .txt:)") + ".txt"

bug_title= str(input("Enter Bug Title:"))
platform = str(input("Enter Platform Type: "))
os = str(input("Enter OS Version: "))
driver = str(input("Enter Driver Version: "))
description = str(input("Describe the issue briefly: "))

with open (filename, "w") as file:
    file.write("---------------BUG REPORT---------------\n")
    file.write(f"Title: {bug_title}\n")
    file.write(f"Platform: {platform}\n")
    file.write(f"OS Version: {os}\n")
    file.write(f"Driver Version: {driver}\n")
    file.write(f"Bug Description: {description}\n")


print("\nReport saved as: ", filename)