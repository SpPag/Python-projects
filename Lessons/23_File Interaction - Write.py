"""
Now to see the "write" mode. I could open the same file as before, but I want to first showcase a property of both the
"append" mode and the "write" mode. They will create a new file with the given name at the specified location, if one
isn't found.
"""

test_file = open("../Test1.txt", "w")
test_file.write("There are mode classes in Grim Dawn!")
test_file.close()

# I'm gonna see if I can create a file in PyCharm's directory, so I can open it and read it without code, inside
# PyCharm. Notice that the file was created by merely asking the code to open the file in "write" mode. I didn't tell
# it to actually write anything in it.

new_file_in_python_directory = open("/Much Test Such Wow.txt",
                                    "w")
new_file_in_python_directory.close()

# Anyway moving on, if we open something in "write" mode, whatever I tell the code to write to the file will replace
# the contents of the file. It won't be added to the end of the file, that's what the "append" mode is for.
