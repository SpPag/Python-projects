# A while loop allows us to execute multiple lines of code until the condition we have set is no longer met
# Let's make a short loop that adds 1 to the value of h until h > 10
'''
h = 1
while h <= 10:
    print(h)
    # Now I want to type h = h + 1, but a shorthand way to do that is the following
    h += 1
print("Escaped the loop")
'''
# There are a few more keywords that we can use with the "while" command. One is "break", that forcibly breaks the loop.
# Another is "continue", that forcibly continues the loop.
# Finally, we can use the "else" keyword to tell the code what to do if the condition isn't met. Which I guess we did
# in the previous example by merely coding after the loop.
h = 1
while h < 8:
    print("h is less than 8")
    h += 1
    if h == 7:
        break
else:
    print("h is no longer less than 8")
# As soon as h became equal to 7, the "break" command broke the loop.
h = 1
while h < 8 or h != 10:
    print("h is less than 8 and equal to " + str(h))
    h += 1
    if h == 8:
        continue
else:
    print("h is no longer less than 8 or different than 10")
# In this example, when h became equal to 8, instead of the loop breaking, we forced it to continue with the
# "continue" command. I added the != 10 stuff to prevent it from going on forever.
