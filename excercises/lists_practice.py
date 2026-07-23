balances = [1000, 1200, 1450, 1710]
print(balances[0])
print(balances[2])
print(balances[-1])

latest_balance = balances[-1]
print(f"Latest balance: £{latest_balance:.2f}")

balances.append(2000)

print(balances)
print(f"Number of balances: {len(balances)}")
print(f"New latest balance: £{balances[-1]:.2f}")

for balance in balances:
    print(f"Year-end balance: £{balance:.2f}")

for balance in balances:
    increased_balance = balance * 1.05
    print(f"Balance after 5% growth: £{increased_balance:.2f}") 


starting_balance = 1000
annual_return = 5
number_of_years = 5

yearly_balances = []
current_balance = starting_balance

for year in range(number_of_years):
    current_balance = current_balance * (1 + annual_return / 100)
    yearly_balances.append(current_balance)

year = 1

for balance in yearly_balances:
    print(f"Year {year}: £{balance:.2f}")
    year = year + 1

print(f"\nTotal years: {len(yearly_balances)}")
print(f"Starting balance: £{starting_balance:.2f}")
print(f"Final balance: £{yearly_balances[-1]:.2f}")

total_growth = yearly_balances[-1] - starting_balance
print(f"Total growth: £{total_growth:.2f}")