def say_hello():
    print("Hello")

say_hello()

def greet(name):
    print(f"Hello {name}")

greet("Kyle")

def add_numbers(a, b):
    return a + b

result = add_numbers(5, 10)

print(result)

def calculate_tax(salary):
    if salary < 50000:
        return salary * 0.8
    else:
        return salary * 0.6

net_salary = calculate_tax(int(input("Enter your salary: ")))
    
print(net_salary)