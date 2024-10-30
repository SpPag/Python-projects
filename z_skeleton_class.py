class Skeleton:
    def __init__(self, hitpoints, weapon, armor, type="regular"):
        self.hitpoints = hitpoints
        self.weapon = weapon
        self.armor = armor
        self.type = type
        self.original_hitpoints = hitpoints
        print("A skeleton appears!")

    def take_damage(self, damage):
        if self.type.lower() == "enchanted":
            damage = round(damage / 1.5)
        if damage >= self.original_hitpoints:
            print("You destroyed the skeleton with one hit!")
        elif self.original_hitpoints / damage <= 2:
            print("Your attack connected and you dealt significant damage!")
        elif self.original_hitpoints / damage > 2:
            print("Your attack connected and the skeleton appears weakened, if slightly.")
        self.damage = damage
        self.hitpoints -= damage

    def check_life(self):
        if self.hitpoints > 0:
            print(f"{self.hitpoints} hitpoints remaining.")
        elif self.hitpoints <= 0:
            print("The skeleton crumbles!")

    def __str__(self):
        if self.weapon[0].lower() in "a, e, i, o, u, y":
            return (f"This is a {self.type} skeleton and has {self.hitpoints} hitpoints, uses an {self.weapon} and "
                    f"wears {self.armor} armor.")
        elif self.weapon[0].lower() not in "a, e, i, o, u, y":
            return (f"This is a {self.type} skeleton and has {self.hitpoints} hitpoints, uses a {self.weapon} and wears"
                    f" {self.armor} armor.")


skeleton_1 = Skeleton(20, "mace and shield", "hide", "enchanted")
print(skeleton_1)
skeleton_2 = Skeleton(20, "bow and arrow", "hide", "regular")
print(skeleton_2)

skeleton_1.take_damage(8)
skeleton_1.check_life()
skeleton_2.take_damage(8)
skeleton_2.check_life()
