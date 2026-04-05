#Add this function inside EmployeeDetails class
def update_employee(self):
    print("\n--- Update Employee ---")
    name = input("Enter employee name to update: ")

    if name not in self.employee_records:
        print("Employee not found!")
        return

    print("Enter new details:")

    salary = float(input("New Salary: "))
    allowance = float(input("New Allowance: "))
    deductions = float(input("New Deductions: "))
    pan_number = input("New PAN Number: ")

    # PAN validation
    if pan_number in self.set_pan:
        print("PAN already exists! Update cancelled.")
        return

    # remove old PAN and add new one
    old_pan = self.employee_records[name][3]
    self.set_pan.remove(old_pan)
    self.set_pan.add(pan_number)

    # update record
    self.employee_records[name] = [salary, allowance, deductions, pan_number]

    print("Employee updated successfully!")



    ## in db.py
    def update_employee():
    id = int(input("Enter ID to update: "))
    salary = float(input("New salary: "))

    cur.execute("""
        UPDATE employees
        SET salary = %s
        WHERE id = %s
    """, (salary, id))

    conn.commit()
    print("Updated successfully")