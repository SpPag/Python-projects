# A tuple is a data type, very similar in form a list, but with one key difference. They cannot be modified in any way.
# The way to define a tuple is, again very similar to the way to define a list. Instead of [], though, you use ().
camping_coordinates = (38.16726, 23.73465)
print("camping spot A: " + str(camping_coordinates))
# It makes sense for tuples to be used for pieces of information that are not going to change. A good example of such
# information, is a set of coordinates.
# A list can also be comprised of tuples
camping_spots = [(38.1665113089647, 23.733900527758447), (38.0739635648433, 22.984653983623765)]
print("camping spots: " + str(camping_spots))
