"""
Coding a function that rolls a num-sided die, to use in the "Modules - Bigger File" file. We need to import the "random"
database or whatever it's called because, I'm interpreting, that is what simulates the die roll. The first value in the
parentheses is the lowest possible number we want to be able to roll and the second is the highest possible number we
want to be able to roll.
"""

import random


def roll_dice(num):
    return random.randint(1, num)
