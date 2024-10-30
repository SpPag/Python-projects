"""original number 121
Yes. given number is palindrome number

original number 125
No. given number is not palindrome number"""

num = input("provide a whole number to check if it's a palindrome: ")
num_reversed = ""
try:
    num_int = int(num)
    for digit in num:
        num_reversed = digit + num_reversed # smart way to practically add something to the beginning of a string
    if num_reversed == num:
        print(f"{num} is a palindrome.")
    elif num_reversed != num:
        print(f"{num} is not a palindrome.")
except Exception as error:
    print(error)
