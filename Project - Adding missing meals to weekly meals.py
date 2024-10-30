import z_replace_in_reverse_function
available_options = ["κοτόπουλο", "μοσχάρι", "λαδερό", "όσπρια", "θαλασσινό", "μακαρονάδα", "ελεύθερο"]
mealslist = ["κοτόπουλο", "μοσχάρι", "λαδερό", "λαδερό"]

"""
another idea was to use a boolean for each meal option like this:
if "κοτόπουλο" not in mealslist:
    needs_chicken = True
"""

needs = ""
for option in available_options:
    if option not in mealslist:
        needs += option + ", "
needs = z_replace_in_reverse_function.r_replace(needs, ", ", ".", 1)
if needs != "":
    print(f"You didn't have these last week: {needs}")
new_meal = input("Meal: ").lower()
if new_meal in needs:
    needs = needs.replace(new_meal + ", ", "")
print(needs)
try:
    needed_meals = open("Needed meals.txt", "r+", encoding="utf-8")
except FileNotFoundError:
    needed_meals = open("Needed meals.txt", "w", encoding="utf-8")
    needed_meals.close()
    needed_meals = open("Needed meals.txt", "r+", encoding="utf-8")
    needed_meals.write(needs)
    needed_meals.close()