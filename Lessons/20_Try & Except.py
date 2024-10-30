# If we code something wrong or ask for input expecting the user to input a number for example, but they input a
# string, when the code is run it will show an error and crash. We may usually not want that. We can handle that
# in a different way, by making the code print a reason for why something wasn't correct, but that print will still
# be part of the code, it won't be crashing.


# number = int(input("Enter a number: "))
# print(number)


# The above code runs just fine if we input a number. But what if we input text? It crashes.
# This is where the try and except keywords come in.


# try:
#    number = int(input("Enter a number: "))
#    print(number)
# except:
#    print("Invalid input")


# Now this isn't perfect either, because what the keyword "except" does as is, is that regardless of the specific
# error that crashes the code, it's going to print "Invalid input". What if the error wasn't an invalid input error?
# We can specify the error in response to which, the "except" block runs. If we run the first piece of code and
# input i.e. "f" instead of a number, the error will read "ValueError: invalid literal for int() with base 10: 'f'
# From that we can see that the error's type is "ValueError". To showcase the reason why we don't want to leave it
# as just "except" I will add a line that includes an error, which is division by zero. Again, we run the code and
# this time see that the error's type is "ZeroDivisionError".
# Finally, we can store the value of an error in a variable inside the "except" command and print that, so that we
# can better see precisely what went wrong and not depend on the programmer's comment being accurate.

try:
    this_is_wrong = 10 / 0
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as error:
    print(error)
except ValueError:
    print("Invalid input")
else:
    print("No division by zero or value errors detected.")  # the else code runs if no except code was run
finally:
    print("This final code line always runs")

"""
I can also use "except Exception as error:" to store the error description, WHATEVER THE ERROR MAY BE, in the "error"
variable, and perhaps afterwards print it. Maybe like this:
try:
    this_is_wrong = 10 / 0
    number = int(input("Enter a number: "))
    print(number)
except Exception as error:
    print(error)
"""
