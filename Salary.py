# To calculate the Gross salary of an employee
print("Enter your basic salary: ", end='')
b = int(input())
# The salary components
DA = (25/100) * b
HRA = (15/100) * b
PF = (12/100) * b
TA = (7.50/100) * b
Net_Pay = b + DA + HRA + TA
Gross_Pay = Net_Pay - PF

print("Your Gross pay is: ", end='')
print(Gross_Pay)