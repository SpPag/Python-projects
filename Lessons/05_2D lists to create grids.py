# we'll make a list, the elements of which, are lists themselves

number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]
# in order to print something from the list, we first indicate the list's element. So [1] is the second
# element (that is, the list: [4, 5, 6]). Now, in order to indicate which element from that list we want
# to print, we use another set of [] after the first one.

print(number_grid[1])
print(number_grid[1][1])

# I'd like to point out that the grid is just for aesthetics. Tutorial guy said that the first []
# refers to the row and the second [] to the column. That is not the case, as demonstrated below.

number_grid = [
    [1, 2, 3],
    [4, 5, 6],
       [7, 8, 9],
    [0]
]

print("According to Tutorial guy the following should print \"7\"")
print("I think it will print \"8\"")
print(number_grid[2][1])

# anyway, moving on
number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

for element in number_grid:
    print(element)

for element in number_grid:
    for elements_element in element:
        print(elements_element)
