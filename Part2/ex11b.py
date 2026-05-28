def calculate(num1, operator, num2):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        return num1 / num2
print(calculate(10, "+", 10))  # 20
print(calculate(10, "-", 10))  # 0
print(calculate(10, "*", 10))  # 100
print(calculate(10, "/", 10))  # 1.0