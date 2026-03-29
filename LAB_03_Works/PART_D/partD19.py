def add_numbers(a, b):
    return a + b

# Take input from user
x, y = map(int, input("Enter two numbers: ").split())
print("Sum =", add_numbers(x, y))