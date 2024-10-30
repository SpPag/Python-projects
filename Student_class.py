"""
Classes are a big part of Python. Regarding data types, so far we've seen strings, numbers, boolean values, lists, sets,
and tuples. Those, however, are not enough on their own to describe i.e. a real world human being. In cases where the
preexisting data types can't cover owr needs we can use the "class" function to define our own data type. I'll follow
"Tutorial guy"'s example to illustrate the "class" function.
"""


class Student:
    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation


'''
So with that we have created a new class, that we have named "Student". The "__init__" thing is the "initialize"
function. It's needed to create the new data type. The "self" part wasn't explained by "Tutorial guy" but I guess it's
mandatory. The rest of the elements inside the parentheses are basically prompts for the information the function needs.
Below that, with all the "self.name" etc stuff we are assigning the values that the prompts are given by the coder to
the function so that it can run. Following "Tutorial guy"'s example, I will import this into another file to run it
there. It is good practice I think to keep the "import" command in mind and also this time we'll see how to grab a
piece of information from a specific file. 
'''
