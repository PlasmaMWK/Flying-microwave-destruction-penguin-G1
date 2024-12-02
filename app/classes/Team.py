class Team:

    def __init__(self, name):
        self.name = name
        self.characters = []
        self.tank = None

    def add_character(self, character, tank=False):
        self.characters.append(character)
        if tank:
            self.tank = character

    def get_characters(self):
        return self.characters

    def get_hp(self):
        return sum(character.get_hp() for character in self.characters)

    def is_alive(self):
        return self.get_hp() > 0

    def is_dead(self):
        return self.get_hp() <= 0

    def get_name(self):
        return self.name
    
    def get_tank(self):
        return self.tank