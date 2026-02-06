# AIM: Design a Python program to compute 
# the factorial of a given integer N.
# Coder: Shifaa
# Date: 06/02/2026

print("--- Factorial Finder ---\n")

# Write your code here

num = int(input("Enter Number: "))

factorial = 1

if num >= 0:
    for i in range(1, num + 1):
       factorial *= i
       print(factorial)
else:
    print("Factorial of" , num , "is Not Defined")
    


