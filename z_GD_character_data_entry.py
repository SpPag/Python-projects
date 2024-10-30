def register_new_char():
    from z_GD_char_class import GDcharacter
    try:
        gd_chars = open("gd_chars", "a")
    except FileNotFoundError:
        gd_chars = open("gd_chars", "w")
        gd_chars.close()
        gd_chars = open("gd_chars", "a")
    y_n_answers = ["Y", "Υ", "N", "Ν"]
    answer = ""
    new = ""
    while answer.upper() not in y_n_answers or answer.upper() == "Y" or answer.upper() == "Υ":
        answer = input("Would you like to register a new character? Y/N\n")
        while answer.upper() not in y_n_answers or answer.upper() == "Y" or answer.upper() == "Υ":
            if answer.upper() == "Y" or answer.upper() == "Υ":
                is_sure = ""
                while is_sure.upper() not in y_n_answers or is_sure.upper() == "N" or is_sure == "Ν":
                    char_name = input("character's name: ")
                    char_class = input("character's class: ")
                    char_level = input("character's level: ")
                    char_weapons = input("character's weapons: ")
                    new = GDcharacter(char_name, char_class, char_level, char_weapons)
                    print("\n", str(new))
                    is_sure = ""
                    while is_sure.upper() not in y_n_answers:
                        is_sure = input("\nAre you sure the data you've given is accurate? Y/N\n")

                gd_chars.write(str(new) + "\n" + "\n")
                again = ""
                while again.upper() not in y_n_answers:
                    again = input("Would you like to register another character? Y/N\n")
                    if again.upper() == "Y" or again.upper() == "Υ":
                        answer = "Y"
                    if again.upper() == "N" or again.upper == "Ν":
                        answer = "N"
    gd_chars.close()
