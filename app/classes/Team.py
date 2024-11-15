#Importing the Character class 
from .Character import Character


class Team:
    """
    A class to represent a team.

    Attributes
    ----------
    name : str
        The name of the team.
    characters : list
        A list to store characters in the team.

    Methods
    -------
    add_character(character):
        Adds a character to the team.
    
    get_characters():
        Returns the list of characters in the team.
    """

    def __init__(self, name):
        self.name = name
        self.characters = []

    def add_character(self, character):
        self.characters.append(character)

    def get_characters(self):
        return self.characters
    
    def perform_attack(attacking_team, defending_team):
    """
    Gère une attaque aléatoire entre un joueur vivant de l'équipe attaquante
    et un joueur vivant de l'équipe défendante.
    """
    # Filtrer les personnages vivants dans les deux équipes
    attackers = [character for character in attacking_team.get_characters() if character.get_hp() > 0]
    defenders = [character for character in defending_team.get_characters() if character.get_hp() > 0]

    if not attackers or not defenders:
        print("Aucune attaque possible : une équipe est entièrement KO.")
        return

    # Choisir un attaquant et une cible
    attacker = random.choice(attackers)
    target = random.choice(defenders)

    # Effectuer l'attaque
    attacker.attack(target)
