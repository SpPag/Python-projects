def char_class_count():
    import random
    available_classes = ["commando", "witchblade", "blademaster", "battlemage", "warder", "tactician", "death knight",
                         "warlord", "pyromancer", "witch hunter", "warlock", "conjurer", "deceiver", "cabalist",
                         "sentinel", "saboteur", "spellbreaker", "trickster", "infiltrator", "reaper", "dervish",
                         "sorcerer", "druid", "mage hunter", "spellbinder", "templar", "elementalist", "vindicator",
                         "ritualist", "archon", "tactician", "purifier", "apostate", "paladin", "defiler", "oppressor",
                         "shield breaker"]
    gd_chars = open("gd_chars", "r")
    gd_charslist = []
    class_and_count = []
    zero_of_these = []
    for line in gd_chars:
        gd_charslist.append(line)
    for gd_class in available_classes:
        class_count = gd_charslist.count("Class: " + gd_class.capitalize() + "\n")
        class_and_count.append(gd_class.capitalize() + ": " + str(class_count))

    for item in class_and_count:
        print(item)
    for item in class_and_count:
        if "0" in item:
            item_name = item.split(":")
            zero_of_these.append(item_name[0])
    print("You don't have any of these", zero_of_these)
    suggestion = random.choice(zero_of_these)
    print("May I suggest a " + suggestion + "?")
    gd_chars.close()
