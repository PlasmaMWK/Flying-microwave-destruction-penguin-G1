
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