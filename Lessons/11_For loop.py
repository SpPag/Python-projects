for letter in "Hello wank":
    print(letter)
# the for function as I've used it above repeats a command for each repetition of the variable I've specified
# in the above set of data

houses = ["Mage", "Acolyte", "Primalist", "Sentinel", "Rogue"]
for chicken in houses:
    print(chicken)

# example with numbers and the "range" function
for pepeNumber in range(0, 10):
    print(pepeNumber)

# the "range(10)" function includes every whole number starting from 0 and finishing just before 10. It is the same
# as "range(0, 10)", we kind of just omit the 0. We can also add one more piece of information to the command, which
# is the step with which to progress along the range. For example, range(1, 10, 3) will get the code to look at the
# numbers 1, 4, 7.

print()

for pepeNumber in range(len(houses)):
    print(houses[pepeNumber])
# so this seemed weird to me at first. len(houses) shows the number of elements inside the list "houses". so
# len(houses) = 5. For the first iteration of the loop, the value of the "pepeNumber" variable is 0.
# for the second iteration it is 1, for the third it is 2, for the fourth it is 3 and for the fifth and last one
# it is 4. So the first iteration's print command is "print(houses[0])", which prints the element inside the list
# "houses" that occupies the 0 position. That is "Mage". Over.

'''
Similarly to while loops, we can use a few more keywords with the for loop. First, the "break" keyword.

fruits = ["apples", "oranges", "bananas"]
for fruit in fruits:
    print(fruit)
    if fruit == "oranges":
        break

The above code will print "apples" as well as "oranges", but then will execute the "break" command since fruit is
equal to "oranges" and break the code (aka stop it from executing further).
We can also use the "continue" keyword, which will force the loop to continue in case it were to break. It would follow
a similar structure to "break", just with "continue" in place of "break".
Finally, we can use the "else" keyword, which will execute once the loop is done. I think this just adds more clutter
to the code though, since we could just code the next step after the loop and it would execute after the loop, anyway.
'''
