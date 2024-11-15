import random

class Player:
    def __init__(self, name: str, hp: int, speed: int):
        self.name = name
        self.hp = hp
        self.speed = speed

    def attack_random_enemy(self: str, other_team: list):
        '''
        First argument if the player that is attacking
        Second argument is the list of players that the player can attack in the other team
        
        Return the name of the player that the player will attack        
        '''
        if not other_team:
            return None
        elif self.hp <= 0:
            return None
        elif enemy.hp <= 0:
            enemy = random.choice(other_team)
        
        enemy = random.choice(other_team)

        return enemy.name

