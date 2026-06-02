import sys 

annual_salary = float(input("what is your annual salary? "))
monthly_expenses = float(input("what are your monthly outgoings? "))
age = int(input("what is your age? "))

if age < 18:
    print("You are not eligible for this service ")
    sys.exit()
      
if annual_salary < 50000:
    tax_rate = 0.20
else: 
    tax_rate = 0.40

monthly_net_salary = annual_salary * (1 - tax_rate) / 12
monthly_savings = monthly_net_salary - monthly_expenses

print(f'Your monthly net salary is: £{monthly_net_salary:.2f}')
print(f'Your monthly savings are: £{monthly_savings:.2f}')

if monthly_net_salary > 4000:
    print("High Income")
else:
    print('Standard Income')

if monthly_savings > 1000:
    print("Excellent Savings")
elif 500 <= monthly_savings <= 1000:
    print("Good Savings")
else:    print("Needs Improvement")



