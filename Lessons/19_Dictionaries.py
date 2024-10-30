# Let's do months like the tutorial guy did
months = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
           }
print(months["Dec"])
# a better way to ask for a value from the dictionary would be by using the get function
print(months.get("Dec", "This isn't in the dictionary"))
print(months.get("Potato","Not a valid key"))
# the .items() command registers all the items inside a dictionary in their preexisting order
print(months.items())
'''
if I want to do something to the dictionary that I cannot, but I could do to a list, I can use the list command to
treat it as a list
'''
months_list = list(months.items())
print(months_list)
'''
now I can for example, sort the contents of the new item, months_list, since it is a list
'''
months_list.reverse()
print(months_list)

'''
example showing how to add entries to a dictionary with user input
'''
contacts = {
    "Adriana": 111222,
    "Georgius": 333444
}
name = input("New contact's name: ")
number = input("New contact's number: ")
contacts[name] = int(number)
print(contacts)

"""
For loops regarding dictionaries can be special. If I use the ".items()" function of a dictionary I get a list, the
elements of which are the pairs of each key with its value. If I then use a for loop with two(!) loop variables for that
list, the loop will assign the key to the first variable and its value to the second variable, each loop iteration.
"""

classmates = {"Emma": "hot", "John": "geek but cool", "Adriana": "to-do list"}

for dict_key, dict_value in classmates.items():
    print(dict_key + " -> " + dict_value)
