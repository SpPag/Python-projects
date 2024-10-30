s1 = "abc"
s2 = "xyz"
# Create a list with all the possible combinations of the letters of s1 and s2.
# First without list comprehension just so I can figure it out.
pepe_list = []
for char1 in s1:
    for char2 in s2:
        pepe_list.append(char1 + char2)
print(pepe_list)

# Now with list comprehension.
pepega_list = [charac1 + charac2 for charac1 in s1 for charac2 in s2]
print(pepega_list)
