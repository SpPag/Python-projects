# Take any piece of text and create a list with tuples, which consist of the first letter of each word and that letter's
# unicode. Reminder: use the ord() function to get the unicode of a character.
text = ("Hello darkness, my old friend I've come to talk with you again Because a vision softly creeping Left its seeds"
        " while I was sleeping And the vision that was planted in my brain Still remains Within the sound of silence")
# Without list comprehension.
list1 = []
for word in text.split():
    tu = (word[0], ord(word[0]))
    list1.append(tu)
print(list1)

text = ("Hello darkness, my old friend I've come to talk with you again Because a vision softly creeping Left its seeds"
        " while I was sleeping And the vision that was planted in my brain Still remains Within the sound of silence")
# With list comprehension.
list2 = [(word[0], ord(word[0])) for word in text.split()]
print(list2)
