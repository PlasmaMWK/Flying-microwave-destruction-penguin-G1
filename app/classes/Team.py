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