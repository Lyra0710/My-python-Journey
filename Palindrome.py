# To check if a number is Palindrome using list slicing

print("Enter a number with at least 2 digits: ", end='')
num = input()

num_r = num[::-1]
if int(num) == int(num_r):
    print(f"{num} is a palindrome")
else:
    print(f"{num} is not a palindrome")
#--------------------------------------------------------------------------
# Other method

# print("Enter a number with at least 2 digits: ", end='')
# num = int(input())
# temp = num
# reverse = 0
# while num > 0:
#     a = num % 10
#     reverse = reverse*10 + a
#     num = num//10  # floor division
#
# if temp == reverse:
#     print(f"{temp} is a palindrome")
# else:
#     print(f"{temp} is not a palindrome")
