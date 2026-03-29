# Program to find the largest of two numbers

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

if a > b:
    print("The largest number is:", a)
elif b > a:
    print("The largest number is:", b)
else:
    print("Both numbers are equal.")