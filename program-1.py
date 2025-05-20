
a = float(input("Enter first number (a): "))
b = float(input("Enter second number (b): "))
operation = input("Enter operation (add, subtract, multiply, divide): ").lower()


if operation == "add":
    result = a + b
elif operation == "subtract":
    result = a - b
elif operation == "multiply":
    result = a * b
elif operation == "divide":
    if b == 0:
        result = "Error: Division by zero"
    else:
        result = a / b
else:
    result = "Error: Invalid operation"
print(f"Result: {result}")
