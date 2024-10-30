print("Integers are whole numbers from the set of negative, positive and 0")
print("Whole numbers are numbers without decimals from the set of positive and 0")
print(2)
print(3.147681253768512)
print(3 + 59 * 2)
print((3 + 59) * 2)
name = "Arch"
age = 29
print("my name is " + name + " and my age is " + str(age))
# You can also use an f string to print numbers along with strings. The syntax for the above result is as follows.
print(f"my name is {name} and my age is {age}")
print("The \"str\" function presents the named parameter as a string. The \"int\" function presents it as an integer")
number = -5
print(abs(number))
print("the \"pow\" function raises the first named number to the power of the second named number")
print(pow(8, 2))
print("The \'max\" and \"min\" functions provide the biggest and smallest numbers respectively from their defined sets")
print(max(1, 2, 9, 200))
print(min(1, 2, 9, 200))
print("The \"round\" function rounds numbers, following \"standard\" rounding rules")
print(round(3.5))
print("In order to use various other functions we need to import them into this file from the \"math\" module. That's "
      "what I'm doing below")
from math import *
print("The \"floor\" and \"ceil\" function round the given number down and up respectively")
print(floor(3.5))
print(ceil(3.5))
print("The \"sqrt\" function gives the square root of the given number")
print(sqrt(81))
print("The \"int\" function presents the named string as an integer. However, that means that the program cannot "
      "handle numbers with decimals. In order to include that, I can use the \"float\" function")
num1 = input("enter a number: ")
num2 = input("enter a number: ")
result = float(num1) + float(num2)
print(result)
