class archer:
    def __init__(self, name, level, weapon, armor):
        self.name = name
        self.level = level
        self.max_hitpoints = 3 + level * 2
        self.weapon = weapon
        self.armor = armor
        self.hitpoints = self.max_hitpoints
    def take_damage(self, damage):
        print("Ugh, that was bad.")
        self.hitpoints -= damage

    def check_life(self):
        if self.hitpoints > 0:
            print(f"{self.hitpoints} hitpoints remaining.")
        elif self.hitpoints <= 0:
            print(f"{self.name} is nearly dead.")

    def level_up(self):
        self.level += 1
        self.max_hitpoints = 3 + self.level * 2
        self.hitpoints = self.max_hitpoints

    def __str__(self):
        if self.weapon[0].lower() in "a, e, i, o, u, y":
            return (f"{self.name} is a level {self.level} archer and has {self.hitpoints} hitpoints, uses an "
                    f"{self.weapon} and wears {self.armor} armor.")
        elif self.weapon[0].lower() not in "a, e, i, o, u, y":
            return (f"{self.name} is a level {self.level} archer and has {self.hitpoints} hitpoints, uses a "
                    f"{self.weapon} and wears {self.armor} armor.")

player_character_1 = archer("Nightingale", 1, "damaged wooden bow and arrow", "hide")
print(player_character_1)
player_character_1.take_damage(2)
print(player_character_1)
player_character_1.level_up()
print(player_character_1)
player_character_1.take_damage(1)
print(player_character_1.max_hitpoints)
print(player_character_1.hitpoints)
