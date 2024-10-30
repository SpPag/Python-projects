num1 = float(input("enter a number: "))
num2 = float(input("enter another number: "))
operator = input("enter the operator: ")

if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "/":
    print(num1 / num2)
else:
    print("Apologies, this calculator can only handle simple math")
operator = input("enter the operator: ")
