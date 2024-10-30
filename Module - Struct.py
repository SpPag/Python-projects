"""
The struct module allows users to convert "regular" data to bytes and vice versa. The first line is the code used to
import the module. The asterisk means "aLL".
"""
from struct import *

# Store as bytes data
"""
The pack function takes two parameters, the format of each following value and then the values. Formats are documented
on the python documentation website, but i is for integer, f for float.
"""
packed_data = pack("iif", 6, 19, 4.73)
print(packed_data)

"""
calcsize is a built-in function in struct that takes one parameter, which is the format of the data you want to see
the size in bytes of. i.e. for one integer calcsize equals 4. That means that if I want to send some data to someone,
or store it somewhere, if that data is just one integer, it will take up 4 bytes.
"""
print(calcsize("i"))
print(calcsize("f"))
print(calcsize("iif"))

# To get byte data back to a readable (by humans) form we use the unpack function
original_data = unpack("iif", packed_data)
print(original_data)
