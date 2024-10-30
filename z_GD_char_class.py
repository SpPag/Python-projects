class GDcharacter:
    def __init__(self, name, mastery_combination, level, weapons):
        self.name = name
        self.mastery_combination = mastery_combination
        self.level = level
        self.weapons = weapons

    def __str__(self):
        return f"Name: {self.name}\nClass: {self.mastery_combination}\nLevel: {self.level}\nWeapon: {self.weapons}"
