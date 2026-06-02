name = input("What is your name? ")

income = float(input("Weekly income: "))
spending = float(input("Weekly spending: "))

savings = income - spending

monthly_savings = savings * 4
yearly_savings = savings * 52
savings_rate = (savings / income) * 100

print("Hello", name)
print("weekly savings:", savings)
print("monthly savings:", monthly_savings)
print("yearly savings:", yearly_savings)
print("savings rate:", savings_rate, "%")

if savings > 200:
    print("Excellent saving habits")

elif savings > 0:
    print("You are saving money")

else:
    print("Warning: Overspending")