Grim_Dawn_Masteries = ["Soldier", "Oathkeeper", "Arcanist", "Necromancer", "Nightblade", "Shaman", "Inquisitor",
                       "Demolitionist", "Occultist"]
print(Grim_Dawn_Masteries)
print(Grim_Dawn_Masteries[0])
print(Grim_Dawn_Masteries[-2])
print(len(Grim_Dawn_Masteries))
Grim_Dawn_Masteries[1] = "Hey"
print(Grim_Dawn_Masteries[1])
print(Grim_Dawn_Masteries)
print(Grim_Dawn_Masteries[0:2])
print(Grim_Dawn_Masteries[0:-2])
print(Grim_Dawn_Masteries[0:7])
print(Grim_Dawn_Masteries[0-2])
Last_Epoch_Masteries = ["Primalist", "Sentinel", "Acolyte"]
print(Last_Epoch_Masteries)
print("Oops, I forgot the Rogue. Let's add it.")
Last_Epoch_Masteries.append("Rogue")
print(Last_Epoch_Masteries)
print("I also forgot the Mage, but let\'s add that between the Primalist and the Sentinel")
Last_Epoch_Masteries.insert(1, "Mage")
print(Last_Epoch_Masteries)
#I'm gonna start using these instead of "print". They're just easier. Oh, ''' works as well.
'''like so'''
#the "remove" function removes an element from the list
Last_Epoch_Masteries.remove("Mage")
print(Last_Epoch_Masteries)
Last_Epoch_Masteries.append("Mage")
print(Last_Epoch_Masteries)
All_Masteries = Grim_Dawn_Masteries + Last_Epoch_Masteries
print(All_Masteries)
#The "pop" function deletes the last element from the list, as in the right-most element
Last_Epoch_Masteries.pop()
Last_Epoch_Masteries.append("Mage")
print(Last_Epoch_Masteries)
#The "index" function tells me the position, the named element occupies in the list, if it's there.
print(All_Masteries.index("Primalist"))
#If the named element is not in the list, an error message will appear saying so and the program will crash
#The "count" function gives us the number of times an element shows up in a list. Had I misstyped i.e. "Mage" twice,
#the "print(All_Masteries.count("Mage")) command would print the number 2
'''the "sort" function sorts a list either alphabetically (if string elements) or in ascending order (if numbers)'''
'''the "reverse" function reverses the order of a list's elements. Nothing to do with alphabetical order etc'''
print("copy")
Last_Epoch_Masteries2 = Last_Epoch_Masteries.copy()
print(Last_Epoch_Masteries2)
print("The \"clear\" function deletes all entries from a list")
Last_Epoch_Masteries2.clear()
print(Last_Epoch_Masteries2)
print("The original remains intact")
print(Last_Epoch_Masteries)
