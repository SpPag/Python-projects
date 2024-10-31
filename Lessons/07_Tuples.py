# A tuple is a data type, very similar in form a list, but with one key difference. They cannot be modified in any way.
# The way to define a tuple is, again very similar to the way to define a list. Instead of [], though, you use ().
camping_coordinates = (71.7283462983, 10.01203980)
print("camping spot A: " + str(camping_coordinates))
# It makes sense for tuples to be used for pieces of information that are not going to change. A good example of such
# information, is a set of coordinates.
# A list can also be comprised of tuples
camping_spots = [(70.1928736748568347789823, 9.123863872), (41.345678765, 11.6969696969)]
print("camping spots: " + str(camping_spots))
