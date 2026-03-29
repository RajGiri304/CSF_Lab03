# Menu-driven calculator program

print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = int(input("Enter choice: "))

# Taking two numbers as input
a, b = map(int, input("Enter two numbers: ").split())

if choice == 1:
    print("Sum =", a + b)

elif choice == 2:
    print("Difference =", a - b)

elif choice == 3:
    print("Product =", a * b)

elif choice == 4:
    if b != 0:
        print("Quotient =", a / b)
    else:
        print("Error: Division by zero is not allowed")

else:
    print("Invalid choice")