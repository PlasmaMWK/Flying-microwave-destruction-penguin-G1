
class Character:
    """
    A class to represent a character in the game.
    Attributes
    ----------
    name : str
        The name of the character.
    speed : int
        The speed of the character.
    hp : int
        The health points of the character, initialized to 100.
    Methods
    -------
    get_name():
        Returns the name of the character.
    get_speed():
        Returns the speed of the character.
    get_hp():
        Returns the health points of the character.
    __str__():
        Returns a string representation of the character.
    """
    def __init__(self, name, speed, hp):
        self.name = name
        self.speed = speed
        self.hp = 100


    

    def get_name(self):
        return self.name

    def get_speed(self):
        return self.speed

    def get_hp(self):
        return self.hp

    def __str__(self):
        return f"Personnage(nom={self.name}, vitesse={self.speed}, hp={self.hp})"
    
    def attack(self, target):
    """
    Permet à un personnage d'attaquer un autre personnage.
    """
    if self.hp <= 0:
        print(f"{self.name} est KO et ne peut pas attaquer.")
        return

    damage = random.randint(1, 10)  # Dégâts aléatoires entre 1 et 10
    target.hp -= damage
    print(f"{self.name} attaque {target.name} et inflige {damage} HP.")

    if target.hp <= 0:
        target.hp = 0
        print(f"{target.name} est maintenant KO.")