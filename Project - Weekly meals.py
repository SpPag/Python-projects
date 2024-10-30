meals = open("Meals.txt", "r+")
available_options = ["κοτόπουλο", "μοσχάρι", "λαδερό", "όσπρια", "θαλασσινό", "μακαρονάδα", "ελεύθερο"]
mealslist_pre = []
if "Weekly meals:\n" not in meals:
    meals.close()
    meals = open("Meals.txt", "w")
    meals.write("Weekly meals:\n")
    meals.close()
    meals = open("Meals.txt", "r+")
for line in meals:
    mealslist_pre.append(line)
mealslist = [i.strip("\n") for i in mealslist_pre if i != "Weekly meals:\n"]
want_to_add = True
while want_to_add:
    end = ""
    wants_to_reset = False
    wants_to_exit = False
    if len(mealslist) < 7:
        todays_meal = ""
        while todays_meal not in available_options:
            print("So far you've had: ", mealslist, "this week.")
            print("options are: ")
            for i in available_options:
                if i not in mealslist:
                    print(i)
            todays_meal = input("\nWhat should be added as today's meal? ").lower()
            if todays_meal in mealslist:
                print(f"You've already had {todays_meal} this week.")
                todays_meal = ""
            elif todays_meal == "reset":
                wants_to_reset = True
                break
            elif todays_meal == "exit" or todays_meal == "break":
                wants_to_exit = True
                break
        if wants_to_exit:
            break
        if todays_meal not in mealslist and todays_meal != "reset":
            mealslist.append(todays_meal)
            meals.write(todays_meal + "\n")
            print("\nIncluding today's meal, you've had ", mealslist, "this week")
    if len(mealslist) == 7 or wants_to_reset:
        print("\nSeven meals have been registered. List resetting.\n")
        mealslist = []
        meals.close()
        meals = open("Meals.txt", "w")
        meals.write("Weekly meals:\n")
        meals.close()
        meals = open("Meals.txt", "r+")
        end = ""
        wants_to_reset = False
    y_n_answers = ["Y", "Υ", "N", "Ν"]
    while end not in y_n_answers:
        end = input("\nIs that it?\nY / N\n").upper()
        if end == "Y" or end == "Υ":
            print("\nExiting. So far you've had: ", mealslist, "this week.")
            want_to_add = False
            break
        elif end == "N" or end == "Ν":
            continue
meals.close()
