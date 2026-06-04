def calculate_tax_rate(salary):
    return 0.8 if salary < 50000 else 0.6


def calculate_monthly_net_salary(salary, tax_rate):
    return salary * tax_rate / 12

def calculate_savings(salary, expenses):
    return salary - expenses

def classify_income(net_salary):
    if net_salary > 4000:
        return "Very High income"
    elif net_salary > 2000:
        return "High income"
    elif net_salary > 0:
        return "standard income" 
    
def classify_savings(savings):
    if savings > 1000:
        return "High savings"
    elif savings > 500:
        return "Medium savings"
    else:
        return "Low savings"

salary = float(input("Enter your salary: "))
tax_rate = calculate_tax_rate(salary)
net_salary = calculate_monthly_net_salary(salary, tax_rate)
expenses = float(input("enter your monthly expenses: "))
savings = calculate_savings(net_salary, expenses)

print(f"Your monthly net salary is: £{net_salary:.2f}")
print(f"Your monthly savings are: £{savings:.2f}")
print(f"Your income level is: {classify_income(net_salary)}")
print(f"Your savings level is: {classify_savings(savings)}")

