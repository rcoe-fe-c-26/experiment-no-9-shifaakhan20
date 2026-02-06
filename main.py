# AIM: Design a Python program to compute 
# the factorial of a given integer N.
# Coder: Shifaa
# Date: 06/02/2026

print("--- Factorial Finder ---\n")

# Write your code here

n = int(input("Enter Number: "))

if n < 0:
    print(f"Factorial of {n} is Not Defined")
else:
    fact = 1
    for x in range(1, n + 1):
        fact = fact * x
    print(f"Factorial of {n} is {fact}")
    
