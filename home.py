import psycopg2
from db import get_connection

conn = get_connection()


print("----------------Welcome to the Taxation System---------------------")
##########################  Asmita Task ##########################"

def create_table():
    with conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                CREATE TABLE IF NOT EXISTS employees (
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(100) NOT NULL,
                    salary FLOAT NOT NULL,
                    allowance FLOAT NOT NULL,
                    deductions FLOAT NOT NULL,
                    pan_number VARCHAR(20) UNIQUE NOT NULL
                );
                """
            )
            print("Employee Table created successfully")


create_table()

class EmployeeDetails:
    
    def input_employee_details(self):
        while True:
            try:
                with conn:
                    with conn.cursor() as cur:

                        print("Enter employee details:")
                        name = input("Name: ")
                        salary = float(input("Monthly Salary: "))
                        allowance = float(input("Allowances: "))
                        deductions = float(input("Deductions: "))
                        pan_number = input("PAN Number: ")
                        
                        cur.execute(
                            """
                            INSERT INTO employees (name, salary, allowance, deductions, pan_number)
                            VALUES (%s, %s, %s, %s, %s);
                            """,
                            (name, salary, allowance, deductions, pan_number)
                        )
                        conn.commit()
                        print(f"Employee {name} added successfully.")
                        
                        
            except psycopg2.errors.UniqueViolation:
                print("PAN already exists. Please try entering a different PAN number.")

            choice = input("Do you want to add more employee records? (yes/no): ")
            if choice.lower() != 'yes':
                break
    ####-------Anuska Task-----#####
    def update_employee(self):
        print("\n--- Update Employee ---")
        pan_number = input("Enter PAN number of employee to update: ").strip()

        try:
            with conn:
                with conn.cursor() as cur:   
                    #  Find employee by PAN
                    cur.execute("SELECT * FROM employees WHERE pan_number = %s", (pan_number,))
                    record = cur.fetchone()

                    if not record:
                        print("Employee not found!")
                        return

                    #  Input new details (leave blank to keep old)
                    name = input(f"New Name [{record[1]}]: ") or record[1]
                    salary_input = input(f"New Salary [{record[2]}]: ")
                    salary = float(salary_input) if salary_input else record[2]
                    allowance_input = input(f"New Allowance [{record[3]}]: ")
                    allowance = float(allowance_input) if allowance_input else record[3]
                    deductions_input = input(f"New Deductions [{record[4]}]: ")
                    deductions = float(deductions_input) if deductions_input else record[4]

                    #  Update PAN if needed
                    new_pan = input(f"New PAN [{record[5]}]: ") or record[5]

                    #  Check if new PAN exists in other records
                    if new_pan != pan_number:
                        cur.execute("SELECT * FROM employees WHERE pan_number = %s AND id != %s", (new_pan, record[0]))
                        if cur.fetchone():
                            print("PAN already exists! Update cancelled.")
                            return

                    #  Update employee in DB
                    cur.execute("""
                        UPDATE employees
                        SET name=%s, salary=%s, allowance=%s, deductions=%s, pan_number=%s
                        WHERE id=%s
                    """, (name, salary, allowance, deductions, new_pan, record[0]))
                    
                    conn.commit()
                    print(f"Employee with PAN {pan_number} updated successfully!")

        except Exception as e:
            print("Error updating employee:", e)
   
#main execution
emp_obj = EmployeeDetails()
emp_obj.input_employee_details()

# Call the update function
emp_obj.update_employee()






'''
-----------------Guys you can continus from this--------


class CalculateTax:
    ########################## Task ##########################"
    tax_slabs = (
    (0, 50000, 0.01),
    (50000, 100000, 0.10),
    (100000, float('inf'), 0.20))

    @staticmethod
    def calculate_tax(income):
        if income <= CalculateTax.tax_slabs[0][1]:
            tax = income * CalculateTax.tax_slabs[0][2]
            
        elif income <= CalculateTax.tax_slabs[1][1]:
            tax = income * CalculateTax.tax_slabs[1][2]
                
        else:
            tax = income * CalculateTax.tax_slabs[2][2]
        
        return tax

##########################   Task ##########################"  
class TaxReport:
    def display_report(self, employee_records):
        print("\n-------------------TAXATION Report-------------------")
        print("Employee Name\tEmployee Salary\tAllowances\tDeductions\tPAN Number\tTax Amount\tFinal Salary")

         # ------------------- Anuska Task -------------------
        slab_count = {"low": 0, "mid": 0, "high": 0}
        highest_tax = 0
        highest_taxpayer = ""
        
    # -------------------  Task -------------------

        for name, details in employee_records.items():
            salary, allowance, deductions, pan_number = details
            taxable_income = salary + allowance - deductions
            tax_amount = CalculateTax.calculate_tax(taxable_income)
            final_salary = taxable_income - tax_amount

                # ------------------- Anuska Task -------------------
            # Highest taxpayer
            if tax_amount > highest_tax:
                highest_tax = tax_amount
                highest_taxpayer = name

            # Count employees per tax slab
            if taxable_income <= 50000:
                slab_count["low"] += 1
            elif taxable_income <= 100000:
                slab_count["mid"] += 1
            else:
                slab_count["high"] += 1

           
            # -------------------  Task -------------------

            print(f"{name}\t\t{salary}\t\t{allowance}\t\t{deductions}\t\t{pan_number}\t\t{tax_amount:.2f}\t\t{final_salary:.2f}")
        ## Anuska Task
        print("\n--- Summary ---")
        print(f"Highest Taxpayer: {highest_taxpayer} (Tax: {highest_tax:.2f})")
        print(f"Employees per Tax Slab: {slab_count}")
      


report = TaxReport()
report.display_report(emp_obj.employee_records)
'''