'''
Let's start by opening the same file as in the previous guide.
'''

test_file = open("../Test.txt", "r")

print(test_file.readable())
print(test_file.read())
test_file.close()

'''
Cool we can see it exists and is successfully opened. We can also see its content. Now let's open it in "append" mode.
When we open a file in "append" mode we can only add stuff to the end of the file. Let's add the sentence "There are
more classes in Grim Dawn!".
'''

# test_file = open("C:\\Users\\Alice\\Desktop\\Python Test Files\\Test.txt", "a")
# test_file.write("There are more classes in Grim Dawn!")
# test_file.close()

'''
By opening the file (either manually or through Python) I can see that the sentence has been added.

NOTE: If I rerun this program, it will add the sentence again and again every single time. That's what I've coded it to
do.

So keep that in mind in order to not mess it up.

Now, the end of the file is after the exclamation mark of the last sentence I added. Not at a new line, but right after
the exclamation mark. So if I rerun the code it will add the sentence without starting at a new line. That might not be
the intended behaviour or a good look for that matter. We can tell our code to start a new line with the escape
character "\\n" (obviously one of the slashes had to be added, because Python. The escape character only has one slash).
'''

test_file = open("../Test.txt", "a")
test_file.write("\nThere are more classes in Grim Dawn!")
test_file.close()
