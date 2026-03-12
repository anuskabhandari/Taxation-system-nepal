def save_tax_record(name, salary, tax):
    file = open("tax_records.txt", "a")   # "a" means append (add new data)
    file.write(f"Name: {name}, Salary: {salary}, Tax: {tax}\n")
    file.close()