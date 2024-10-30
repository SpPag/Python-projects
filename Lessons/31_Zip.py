first = ["Shaman", "Nightblade", "Soldier"]
second = ["Druid", "Rogue", "Sentinel"]

names = zip(first, second)
print(type(names))

"""
The zip type object we've named \"names\" looks like a list. Its elements are tuples made up of one element from each of
the lists we've specified. If one list is longer than the other, then the last tuple to be added to the zip will be the
last possible pair of values from the lists. So any values that don't have pairs in the other list won't be included in
the zip at all. We can also use the zip function to combine elements from more than two lists. This example shows two
just for ease of understanding and demonstration.
"""

for x in names:
    print(x)

for i, j in names:
    print(f"{j} in Last Epoch is kind of like {i} from GD")

"""
Both for loops run just fine separately, they just don't run well together. I don't know why.
Answer: Iterators only iterate through each of their values once (deliberately, e.g. to reduce memory use).
To iterate over the same values again, a new Iterator must be created.
So the correct code for that is:
"""

for x in zip(first, second):
    print(x)

for i, j in zip(first, second):
    print(f"{j} in Last Epoch is kind of like {i} from GD")

"""
I've also applied something suggested to me on the post regarding my not being able to iterate through the names
variable twice, which is that instead of creating a new variable (namely names) for the zip object, I just applied
the for loop to the zip object directly. This saves a few lines of code and makes the code less cluttery.
"""
