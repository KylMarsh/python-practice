import sys

def calculate_annual_tax(salary, tax_rate) :
    tax_decimal = tax_rate / 100
    annual_tax = salary * tax_decimal
    return annual_tax

def calculate_monthly_net_salary(salary, annual_tax) :
    annual_net_salary = salary - annual_tax
    monthly_net_salary = annual_net_salary / 12
    return monthly_net_salary

annual_salary = float(input("Enter annual salary: £ "))
tax_rate = float(input("Enter tax rate (%): "))
annual_tax = calculate_annual_tax(annual_salary, tax_rate)
monthly_net_salary = calculate_monthly_net_salary(annual_salary, annual_tax)

if annual_salary < 0:
    print("Salary cannot be negative.")
    sys.exit()
if tax_rate < 0 or tax_rate > 100:
    print("Tax rate must be between 0 and 100.")
    sys.exit()

print(f"\nAnnual tax: £{annual_tax:.2f}")
print(f"Monthly net salary: £{monthly_net_salary:.2f}")
