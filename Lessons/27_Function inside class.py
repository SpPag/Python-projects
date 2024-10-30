'''
We can include multiple functions inside a class. Functions can help classes provide much additional information to the
user, so it's a good idea when we create classes to think about what functions we might want to add to the class. In
this example I have created the class "Student", giving it prompts for three pieces of information: name, major and gpa.
However, I wanted to add one function that can easily tell the user whether the student in question has earned a high
enough gpa to be on honor roll.
'''
from Student_class_with_function import Student

student1 = Student("John", "architecture", 3.0)
student2 = Student("Helena", "medicine", 3.9)

print(Student.is_on_honor_roll(student1))
print(Student.is_on_honor_roll(student2))
