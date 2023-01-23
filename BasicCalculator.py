# Calculator
print("Enter first number: ", end='')
a = int(input())
print("Select Operation: ", end='')
op = input()
print("Enter second number: ", end='')
b = int(input())

def add(a, b):
    return a+b
def subtract(a, b):
    return a-b
def multiply(a, b):
    return a*b
def divide(a, b):
    return a/b

if op=='add':
    r = add(a, b)
    print(f"The sum is {r}")
elif op == "subtract":
    r = subtract(a, b)
    print(f"The difference is {r}")
elif op == "multiply":
    r = multiply(a, b)
    print(f"The product is {r}")
else:
    r = divide(a, b)
    print(f"The quotient is {r}")