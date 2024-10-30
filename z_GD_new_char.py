def new_char():
    available_masteries = ["soldier", "demolitionist", "occultist", "nightblade", "arcanist", "shaman", "inquisitor",
                           "necromancer", "oathkeeper"]

    available_classes = ["commando", "witchblade", "blademaster", "battlemage", "warder", "tactician", "death knight",
                         "warlord", "pyromancer", "witch hunter", "warlock", "conjurer", "deceiver", "cabalist",
                         "sentinel",
                         "saboteur", "spellbreaker", "trickster", "infiltrator", "reaper", "dervish", "sorcerer",
                         "druid",
                         "mage hunter", "spellbinder", "templar", "elementalist", "vindicator", "ritualist", "archon",
                         "tactician", "purifier", "apostate", "paladin", "defiler", "oppressor", "shield breaker"]

    list_for_grid = [["    X    ", "soldier", "demolitionist", "occultist", "nightblade", "arcanist", "shaman",
                      "inquisitor", "necromancer", "oathkeeper"], ["soldier"], ["demolitionist"], ["occultist"],
                     ["nightblade"], ["arcanist"], ["shaman"], ["inquisitor"], ["necromancer"], ["oathkeeper"]]
    option = ""
    mastery_combination = ""
    while option != "1" and option != "2" and option != "3":
        option = input("type 1 to pick masteries by typing their names or 2 to pick from the 2D grid, or you can type "
                       "3 to select a class right away: ")
        if option == "1":
            mastery1 = ""
            mastery2 = ""
            while mastery1.lower() not in available_masteries:
                mastery1 = input("\nType your first mastery: ")
            while mastery2.lower() not in available_masteries:
                mastery2 = input("Type your second mastery: ")
            mastery_combination = mastery1 + "-" + mastery2
            mastery_combination = mastery_combination.lower()
        if option == "2":
            d1 = {1: "soldier",
                  2: "demolitionist",
                  3: "occultist",
                  4: "nightblade",
                  5: "arcanist",
                  6: "shaman",
                  7: "inquisitor",
                  8: "necromancer",
                  9: "oathkeeper"}
            for element in list_for_grid:
                print(element)
            print()
            mastery1 = ""
            mastery2 = ""
            while mastery1 not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                mastery1 = input("Type the number of the column that corresponds to your first mastery: ")
            while mastery2 not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                mastery2 = input("Type the number of the row that corresponds to your second mastery: ")
            mastery_combination = d1[int(mastery1)] + "-" + d1[int(mastery2)]
        if option == "3":
            class_selection = ""
            while class_selection not in available_classes:
                class_selection = input("What class would you like to pick?\n").lower()
            if class_selection == "commando":
                mastery1 = "Soldier"
                mastery2 = "Demolitionist"
            elif class_selection == "witchblade":
                mastery1 = "Soldier"
                mastery2 = "Occultist"
            elif class_selection == "blademaster":
                mastery1 = "Soldier"
                mastery2 = "Nightblade"
            elif class_selection == "battlemage":
                mastery1 = "Soldier"
                mastery2 = "Arcanist"
            elif class_selection == "warder":
                mastery1 = "Soldier"
                mastery2 = "Shaman"
            elif class_selection == "tactician":
                mastery1 = "Soldier"
                mastery2 = "Inquisitor"
            elif class_selection == "death knight":
                mastery1 = "Soldier"
                mastery2 = "Necromancer"
            elif class_selection == "warlord":
                mastery1 = "Soldier"
                mastery2 = "Oathkeeper"
            elif class_selection == "pyromancer":
                mastery1 = "Demolitionist"
                mastery2 = "Occultist"
            elif class_selection == "saboteur":
                mastery1 = "Demolitionist"
                mastery2 = "Nightblade"
            elif class_selection == "sorcerer":
                mastery1 = "Demolitionist"
                mastery2 = "Arcanist"
            elif class_selection == "elementalist":
                mastery1 = "Demolitionist"
                mastery2 = "Shaman"
            elif class_selection == "purifier":
                mastery1 = "Demolitionist"
                mastery2 = "Inquisitor"
            elif class_selection == "defiler":
                mastery1 = "Demolitionist"
                mastery2 = "Necromancer"
            elif class_selection == "shield breaker":
                mastery1 = "Demolitionist"
                mastery2 = "Oathkeeper"
            elif class_selection == "witch hunter":
                mastery1 = "Occultist"
                mastery2 = "Nightblade"
            elif class_selection == "warlock":
                mastery1 = "Occultist"
                mastery2 = "Arcanist"
            elif class_selection == "conjurer":
                mastery1 = "Occultist"
                mastery2 = "Shaman"
            elif class_selection == "deceiver":
                mastery1 = "Occultist"
                mastery2 = "Inquisitor"
            elif class_selection == "cabalist":
                mastery1 = "Occultist"
                mastery2 = "Necromancer"
            elif class_selection == "sentinel":
                mastery1 = "Occultist"
                mastery2 = "Oathkeeper"
            elif class_selection == "spellbreaker":
                mastery1 = "Nightblade"
                mastery2 = "Arcanist"
            elif class_selection == "trickster":
                mastery1 = "Nightblade"
                mastery2 = "Shaman"
            elif class_selection == "infiltrator":
                mastery1 = "Nightblade"
                mastery2 = "Inquisitor"
            elif class_selection == "reaper":
                mastery1 = "Nightblade"
                mastery2 = "Necromancer"
            elif class_selection == "dervish":
                mastery1 = "Nightblade"
                mastery2 = "Oathkeeper"
            elif class_selection == "druid":
                mastery1 = "Arcanist"
                mastery2 = "Shaman"
            elif class_selection == "mage hunter":
                mastery1 = "Arcanist"
                mastery2 = "Inquisitor"
            elif class_selection == "spellbinder":
                mastery1 = "Arcanist"
                mastery2 = "Necromancer"
            elif class_selection == "templar":
                mastery1 = "Arcanist"
                mastery2 = "Oathkeeper"
            elif class_selection == "vindicator":
                mastery1 = "Shaman"
                mastery2 = "Inquisitor"
            elif class_selection == "ritualist":
                mastery1 = "Shaman"
                mastery2 = "Necromancer"
            elif class_selection == "archon":
                mastery1 = "Shaman"
                mastery2 = "Oathkeeper"
            elif class_selection == "apostate":
                mastery1 = "Inquisitor"
                mastery2 = "Necromancer"
            elif class_selection == "paladin":
                mastery1 = "Inquisitor"
                mastery2 = "Oathkeeper"
            elif class_selection == "oppressor":
                mastery1 = "Necromancer"
                mastery2 = "Oathkeeper"
            print(f"{class_selection.capitalize()} is the result of {mastery1} combined with {mastery2}.\nGodspeed!"
                  )

    if "soldier" in mastery_combination:
        if "demolitionist" in mastery_combination:
            mastery_combination = "Commando"
        if "occultist" in mastery_combination:
            mastery_combination = "Witchblade"
        if "nightblade" in mastery_combination:
            mastery_combination = "Blademaster"
        if "arcanist" in mastery_combination:
            mastery_combination = "Battlemage"
        if "shaman" in mastery_combination:
            mastery_combination = "Warder"
        if "inquisitor" in mastery_combination:
            mastery_combination = "Tactician"
        if "necromancer" in mastery_combination:
            mastery_combination = "Death Knight"
        if "oathkeeper" in mastery_combination:
            mastery_combination = "Warlord"
    elif "demolitionist" in mastery_combination:
        if "occultist" in mastery_combination:
            mastery_combination = "Pyromancer"
        if "nightblade" in mastery_combination:
            mastery_combination = "Saboteur"
        if "arcanist" in mastery_combination:
            mastery_combination = "Sorcerer"
        if "shaman" in mastery_combination:
            mastery_combination = "Elementalist"
        if "inquisitor" in mastery_combination:
            mastery_combination = "Purifier"
        if "necromancer" in mastery_combination:
            mastery_combination = "Defiler"
        if "oathkeeper" in mastery_combination:
            mastery_combination = "Shield Breaker"
    elif "occultist" in mastery_combination:
        if "nightblade" in mastery_combination:
            mastery_combination = "Witch Hunter"
        if "arcanist" in mastery_combination:
            mastery_combination = "Warlock"
        if "shaman" in mastery_combination:
            mastery_combination = "Conjurer"
        if "inquisitor" in mastery_combination:
            mastery_combination = "Deceiver"
        if "necromancer" in mastery_combination:
            mastery_combination = "Cabalist"
        if "oathkeeper" in mastery_combination:
            mastery_combination = "Sentinel"
    elif "nightblade" in mastery_combination:
        if "arcanist" in mastery_combination:
            mastery_combination = "Spellbreaker"
        if "shaman" in mastery_combination:
            mastery_combination = "Trickster"
        if "inquisitor" in mastery_combination:
            mastery_combination = "Infiltrator"
        if "necromancer" in mastery_combination:
            mastery_combination = "Reaper"
        if "oathkeeper" in mastery_combination:
            mastery_combination = "Dervish"
    elif "arcanist" in mastery_combination:
        if "shaman" in mastery_combination:
            mastery_combination = "Druid"
        if "inquisitor" in mastery_combination:
            mastery_combination = "Mage Hunter"
        if "necromancer" in mastery_combination:
            mastery_combination = "Spellbinder"
        if "oathkeeper" in mastery_combination:
            mastery_combination = "Templar"
    elif "shaman" in mastery_combination:
        if "inquisitor" in mastery_combination:
            mastery_combination = "Vindicator"
        if "necromancer" in mastery_combination:
            mastery_combination = "Ritualist"
        if "oathkeeper" in mastery_combination:
            mastery_combination = "Archon"
    elif "inquisitor" in mastery_combination:
        if "necromancer" in mastery_combination:
            mastery_combination = "Apostate"
        if "oathkeeper" in mastery_combination:
            mastery_combination = "Paladin"
    elif "necromancer" in mastery_combination:
        if "oathkeeper" in mastery_combination:
            mastery_combination = "Oppressor"
    if option == "1" or option == "2":
        print("Your class is: ", mastery_combination)
    return mastery_combination
