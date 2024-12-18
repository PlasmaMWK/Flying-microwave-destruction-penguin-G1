from app.classes.Weapon import Weapon

class Knife(Weapon):
    def __init__(self, name, damage):
        
        super().__init__(name, damage)