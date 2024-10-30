from z_GD_character_class_count_function import char_class_count
from z_GD_character_data_entry import register_new_char

available_classes = ["commando", "witchblade", "blademaster", "battlemage", "warder", "tactician", "death knight",
                     "warlord", "pyromancer", "witch hunter", "warlock", "conjurer", "deceiver", "cabalist", "sentinel",
                     "saboteur", "spellbreaker", "trickster", "infiltrator", "reaper", "dervish", "sorcerer", "druid",
                     "mage hunter", "spellbinder", "templar", "elementalist", "vindicator", "ritualist", "archon",
                     "tactician", "purifier", "apostate", "paladin", "defiler", "oppressor", "shield breaker"]
y_n_answers = ["Y", "Υ", "N", "Ν"]
marvel = ""
register_new_char()
while marvel not in y_n_answers:
    marvel = input("Would you like to marvel at your characters? Y/N\n").upper()
    if marvel == "Y" or marvel == "Υ":
        gd_chars = open("gd_chars", "r")
        for line in gd_chars:
            print(line)
        gd_chars.close()
    if marvel == "N" or marvel == "Ν":
        print("Very well then, moving on.")
        break

new = ""
while new.upper() not in y_n_answers:
    new = input("Do you wish to create a new character? Y/N\n")
    if new.upper() == "Y" or new.upper() == "Υ":
        wants_to_make_new_character = True
    elif new.upper() == "N" or new.upper() == "Ν":
        wants_to_make_new_character = False
        print("Well then, why are you still here and not out there SLAUGHTERING THE ENEMIES OF MANKIND?!")

while wants_to_make_new_character:
    char_class_count()
    print("Regardless, consider trying a new class!")
    from z_GD_new_char import new_char
    new_char()
    are_we_done_here = input("Are you done here? Y/N\n")
    if are_we_done_here.upper() == "Y" or are_we_done_here.upper() == "Υ":
        wants_to_make_new_character = False
    elif are_we_done_here.upper() == "N" or are_we_done_here.upper() == "Ν":
        continue
    print("Thus a new being is born, ready to combat the horrors of Cairn!")
