# Factorial of a number
print("Enter a number: ", end='')
n = int(input())

factorial = 1

if n == 0:
    factorial = 1
elif n < 0:
    factorial = "NA"
else:
    for i in range(1, n+1):
        factorial = factorial * i

print(f"The factorial of {n} is {factorial}")