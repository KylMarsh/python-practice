name = input("What is your name? ")
salary = float(input("what is your annual salary? "))
expenses = float(input("what is your monthly expenses? "))

savings = (salary / 12) - expenses 
savingspercentage = (savings * 12 / salary) * 100

print(name)
print("Your monthly savings is: ", savings)
print("Your annual savings percentage is: ", savingspercentage, "%")

if savingspercentage >= 20:
    print("Great job! You are saving a good portion of your income. ")

elif savingspercentage >= 0:
    print("You are saving some of your income, this is a good start as every little helps! ")

else:
    print("I see you have negative savings, look into reviewing your expenses!")
      
      
