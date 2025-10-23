def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

# Player input
player_name = input("Enter your name: ")
player_age = int(input("Enter your age (it will not affect the gameplay): "))
a = int(input("Enter the 1st number: "))
b = int(input("Enter the 2nd number: "))

# Operation choose
print("\nChoose an operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
choice = int(input("Enter your choice (1-4): "))

# Performing an operation
if choice == 1:
    print(f'{a} + {b} = {addition(a, b)}')
elif choice == 2:
    print(f'{a} - {b} = {subtraction(a, b)}')
elif choice == 3:
    print(f'{a} * {b} = {multiplication(a, b)}')
elif choice == 4:
    print(f'{a} / {b} = {division(a, b)}')
else:
    print("Invalid choice. Please enter a number between 1 and 4.")
