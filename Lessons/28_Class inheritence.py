'''
When creating a class we may want to model it after another class. In this example I have created the chef class, that
describes a chef that can make a chicken dish, a salad and a special dish (his specialty, which is bbq ribs). After that
I wanted to create another class. One that describes a chinese chef who can make all dishes the previously described
chef can, but his special dish, his specialty, is Beijing duck, and he can also make a fried rice dish.
To code the second class I could have copied the first class' code, but it's way faster (and safer, since it's far less
likely for mistakes to occur) to have it inherit the attributes of the previously created class.
'''
from z_chef_class import Chef
from Chinese_Chef import ChineseChef

myChef = Chef()
myChef.make_special_dish()

myChef = ChineseChef()
myChef.make_special_dish()
myChef.make_fried_rice()

"""
If we have multiple classes that we want a new class to inherit from, we just add all of them in the parentheses. We
cannot leave the class definition entirely blank, so we're adding a "pass" line that does nothing beside preventing a
syntax error.
"""
class Mario():
    def move(self):
        print("I am moving!")

class Shroom():
    def eat_shroom(self):
        print("Now I am big!")

class BigMario(Mario, Shroom):
    pass

bm = BigMario()
bm.move()
bm.eat_shroom()
