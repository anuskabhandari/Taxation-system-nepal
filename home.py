print("-------------------TAXATION SYSTEM OF NEPAL-------------------")
emp_name = []
emp_salary = []
emp_tax = []

while True:

    employee_name = input("Enter employee  name: ")
    if employee_name.strip() == "":
        print("Employee name cannot be empty. Please try again.")
        continue
    if employee_name in emp_name:
        print("Employee name already exists. Please enter a unique name.")
        continue

    employee_salary = float(input("Enter employee salary: "))
    if employee_salary < 0:
        print("Employee salary cannot be negative. Please try again.")
        continue

    tax = employee_salary * 0.1

    emp_name.append(employee_name)
    emp_salary.append(employee_salary)
    emp_tax.append(tax)

    choice = input("Do you want to add another employee? (yes/no): ").strip().lower()
    if choice != 'yes':
        break

print("\n-------------------TAXATION Report-------------------")
print("Employee Name\tEmployee Salary\tTax Amount")
for i in range(len(emp_name)):
    print(f"{emp_name[i]}\t\t{emp_salary[i]}\t\t{emp_tax[i]}")
