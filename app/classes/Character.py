import random


class Character:
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

    def is_alive(self):
        return self.hp > 0

    def is_dead(self):
        return self.hp <= 0

    def attack_random_enemy(self, other_team):
        if not other_team.characters:
            return None
        if self.hp <= 0:
            self.hp = 0
            return None

        alive_enemies = [
            enemy for enemy in other_team.characters if enemy.is_alive()]
        if not alive_enemies:
            return None

        enemy = random.choice(alive_enemies)

        # 5% chance to deal 20 HP damage
        if random.random() < 0.05:
            damage = 20
            enemy.hp -= damage
            if enemy.hp <= 0:
                enemy.hp = 0
                return f"{self.name} kills {enemy.name}!"

            return f"{self.name} attacks {enemy.name} and deals {damage} HP damage."

        # 5% chance for the attack to be reflected back
        if random.random() < 0.05:
            damage = random.randint(1, 10)
            self.hp -= damage
            if self.hp <= 0:
                self.hp = 0
                return f"{self.name} attacks {enemy.name} but kills himself !!"

            return f"{self.name} attacks {enemy.name} but the attack is refleted, he deals {damage} HP damage to himself."

        # Normal attack
        damage = random.randint(1, 10)
        enemy.hp -= damage
        if enemy.hp <= 0:
            enemy.hp = 0
            return f"{self.name} kills {enemy.name}!"

        return f"{self.name} attacks {enemy.name} and deals {damage} HP damage."
