print("----------------Welcome to the Taxation System---------------------")



class EmployeeDetails:
    def __init__(self):
        self.set_pan = set()
        self.employee_records = {}
    def input_employee_details(self):
        while True:
        ##########################  Anuja Task ##########################"
            print("Enter employee details:")
            name = input("Name: ")
            salary = float(input("Monthly Salary: "))
            allowance = float(input("Allowances: "))
            deductions = float(input("Deductions: "))
            pan_number = input("PAN Number: ")

            while pan_number in self.set_pan:
                print("PAN already exists. Enter again.")
                pan_number = input("PAN Number: ")
            self.set_pan.add(pan_number)
                
        ##########################  Anuska Task ##########################"  
            self.employee_records[name] = [salary, allowance, deductions, pan_number]

            choice = input("Do you want to add more employee records? (yes/no): ")
            if choice.lower() != 'yes':
                break



class CalculateTax:
    ##########################  Aiswarya's Task ##########################"
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

##########################  Asmita's Task ##########################"  
class TaxReport:
    def display_report(self, employee_records):
        print("\n-------------------TAXATION Report-------------------")
        print("Employee Name\tEmployee Salary\tAllowances\tDeductions\tPAN Number\tTax Amount\tFinal Salary")

         # ------------------- Anuska Task -------------------
        slab_count = {"low": 0, "mid": 0, "high": 0}
        highest_tax = 0
        highest_taxpayer = ""
        seen_pans = set()
        duplicate_pans = set()
    # ------------------- End Anuska Task -------------------

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

            # Detect duplicate PANs
            if pan_number in seen_pans:
                duplicate_pans.add(pan_number)
            else:
                seen_pans.add(pan_number)
            # ------------------- End Anusk Task -------------------

            print(f"{name}\t\t{salary}\t\t{allowance}\t\t{deductions}\t\t{pan_number}\t\t{tax_amount:.2f}\t\t{final_salary:.2f}")
        ## Anuska Task
        print("\n--- Summary ---")
        print(f"Highest Taxpayer: {highest_taxpayer} (Tax: {highest_tax:.2f})")
        print(f"Employees per Tax Slab: {slab_count}")
        print(f"Duplicate PANs: {duplicate_pans if duplicate_pans else 'None'}")

#main execution
emp_obj = EmployeeDetails()
emp_obj.input_employee_details()

report = TaxReport()
report.display_report(emp_obj.employee_records)