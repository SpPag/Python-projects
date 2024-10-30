"""
In Python, with statement is used in exception handling to make the code cleaner and much more readable. It simplifies
the management of common resources like file streams. Observe the following code example on how the use of with
statement makes code cleaner.
"""

# file handling

# 1) without using with statement
file = open('../Much Test Such Wow.txt', 'w')
file.write('hello world !')
file.close()

# 2) without using with statement
file = open('../Much Test Such Wow.txt', 'w')

try:
    file.write('hello world')
finally:
    file.close()

# using with statement
with open('../Much Test Such Wow.txt', 'w') as file:
    file.write('hello world !')

"""
Notice that unlike the first two implementations, there is no need to call file.close() when using with statement. The
with statement itself ensures proper acquisition and release of resources. An exception during the file.write() call in
the first implementation can prevent the file from closing properly which may introduce several bugs in the code, i.e.
many changes in files do not go into effect until the file is properly closed. The second approach in the above example
takes care of all the exceptions but using the with statement makes the code compact and much more readable. Thus, with
statement helps avoiding bugs and leaks by ensuring that a resource is properly released when the code using the
resource is completely executed. The with statement is popularly used with file streams, as shown above and with Locks,
sockets, subprocesses and telnets etc.

We can use the with statement with objects of user-created classes, as well. We first need to add the __enter__() and
__exit__() functions to the class and assign them a file opening and file closing operation respectively. Example: 
"""

# a simple file writer object

class MessageWriter(object):
    def __init__(self, file_name):
        self.file_name = file_name

    def __enter__(self):
        self.file = open(self.file_name, 'w')
        return self.file

    def __exit__(self, *args):
        self.file.close()


# using with statement with MessageWriter

with MessageWriter('../Much Test Such Wow.txt') as xfile:
    xfile.write('hello world')
