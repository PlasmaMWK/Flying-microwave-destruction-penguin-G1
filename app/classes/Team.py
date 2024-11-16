from .Character import Character


class Team:

    def __init__(self, name):
        self.name = name
        self.characters = []

    def add_character(self, character):
        self.characters.append(character)

    def get_characters(self):
        return self.characters

    def get_hp(self):
        return sum(character.get_hp() for character in self.characters)

    def get_is_alive(self):
        return self.get_hp() > 0

    def get_name(self):
        return self.name
