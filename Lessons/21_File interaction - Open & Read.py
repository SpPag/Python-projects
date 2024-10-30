# We can open files that are on our computers in python with commands. I created a text document on my desktop and
# named it "Test". If it were in the same directory as the python folder that I want to open it from, I can just
# type its name in the "open" command. Otherwise, I need to type its directory path. While typing the path, we need
# to type "\" twice. Typing it once means that we want the following character to be exempt from the quotes. So we
# type it again to indicate that we want the character "\" to be part of the quoted text.
# The open command needs two pieces of information. First is the file to open, either by naming it or its path and
# second is the mode in which to open it. "r" stands for read, "w" stands for write, "a" stands for append and "r+"
# stands for read & write.
# Read only allows us to view the information in the file but not modify it.
# Write only allows us to replace the information in the file, and creates a new file with the given name at the
# specified location if it doesn't exist.
# Read & write allows us to not only view the information in the file but also modify it, but it doesn't create the
# file if it doesn't already exist.
# Append only allows us to add new information to the file, without being able to modify any already existing
# information. It also creates a new file with the given name at the specified location if it doesn't exist.

# There is no "Test.txt" file in this folder, but if there were this would be the command to open it, in read mode.

try:
    open("../Test.txt", "r")
except FileNotFoundError:
    print("File not found in the same directory as python")

print("Trying with specified path")

# Tutorial guy said that we generally want to store the opened file (or the opening of the file to be precise) in a
# variable. He also said, and I get this, that it's a good idea to always make sure we close the file once we're
# done with it. That what the .close command is for.

# Here, as a first step after opening a file, I want to make sure that it's readable. That's what the .readable
# command does. If instead of read mode I open the file in write mode, the readable command will print False.
# The .read command reads the file.

test_file = open("../Test.txt", "r")

print(test_file.readable())
print(test_file.read())
test_file.close()

# The .readline command reads the first line of the file and then "moves the cursor" to the beginning of the next line.
# Inside the parentheses we can specify the number of characters we want read from the line.

'''
print("NEXT")
test_file = open("Test.txt", "r")
print(test_file.readable())
print(test_file.readline())
print(test_file.readline())
print(test_file.readline())
test_file.close()
'''

# Now with the command .readlines we can both read the content of the file and create a list with those elements.
# We can use a set of brackets at the end of the .readlines() command to ask it to only print a specified element
# from the newly created list.

test_file = open("../Test.txt", "r")

print(test_file.readable())
print(test_file.readlines()[0])
test_file.close()

# We can also use a for loop along with the .readlines()[] command to print every element of the list, one at a time.
# Might be useful, just pointing it out.

print("FOR LOOP")
test_file = open("../Test.txt", "r")
for line in test_file.readlines():
    print(line)
test_file.close()
