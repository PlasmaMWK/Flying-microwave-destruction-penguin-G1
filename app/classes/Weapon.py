
class Weapon():
    def __init__(self):
        self.damage = 0.1

    def new_damage(self, damage):
        return damage + self.damage * damage

    def __str__(self):
        return "🗡️"
