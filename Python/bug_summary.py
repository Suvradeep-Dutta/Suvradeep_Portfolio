import csv

filename= "bug_data.csv"
module_count={}

print("====== BUG COUNT REPORT ======\n")

with open(filename, newline='') as file:
    reader= csv.DictReader(file)

    for row in reader:
        module= str(row["Module"])
        if module in module_count:
            module_count[module] += 1
        else:
            module_count[module]= 1
for module, count in module_count.items():
    print(f"        {module} : {count} bugs")


