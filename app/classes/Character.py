import random

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
    def __init__(self, name: str, speed: int):
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
    
    
    def attack_random_enemy(self, other_team):
        """
        Attacks a random enemy from the other team.
        
        Parameters:
        self (Character): The character that is attacking.
        other_team (Team): The team that the character can attack.
        
        Returns:
        str: The name of the enemy that was attacked, or None if no attack was made.
        """
        if not other_team.characters:
            return None
        if self.hp <= 0:
            return None
        
        alive_enemies = [enemy for enemy in other_team.characters if enemy.hp > 0]
        if not alive_enemies:
            return None
        
        enemy = random.choice(alive_enemies)
        print(f"{self.name} attaque {enemy.name}")

        return enemy.name
