balance = float(input("What is your current investment account balance> "))
initial_balance = balance
interest_rate = float(input("What is your expected investment return rate? "))

print(f"Starting balance: £{balance:.2f}")

years = 1
while years <= 10:
    balance = balance * (1 + interest_rate / 100)
    print("After year ", years, " your expected return is:£ ", f"{balance:.2f}")
    years += 1

if balance >= 1.5 * initial_balance:
    print("This is a significant increase on your initial investment!")