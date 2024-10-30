query = ""
while query != "stop":
    num1 = input("Please provide the first whole number of your choice: ")
    num2 = input("Please provide the second whole number of your choice: ")
    while num1.isnumeric() is False or num2.isnumeric() is False:
        print("\nInvalid input, please input whole numbers only.\n")
        num1 = input("Please provide the first whole number of your choice: ")
        num2 = input("Please provide the second whole number of your choice: ")
    sum = int(num1) + int(num2)
    product = int(num1) * int(num2)
    print(sum)
    print(product)
    query = input("Type \"stop\" to exit the program, otherwise press ENTER: ")
