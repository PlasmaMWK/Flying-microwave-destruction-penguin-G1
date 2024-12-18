import random
from classes.Weapon import Weapon


class Character:
    def __init__(self, name: str, speed: int, stamina: int, weapon=None, shield=False):
        self.name = name
        if shield:
            self.speed = speed - 1
        self.speed = speed
        self.stamina = stamina
        self.original_hp = 10 * stamina
        self.hp = self.original_hp
        self.weapon = weapon
        self.shield = shield


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
    
    def action_lib(self, player2, damage, action):
        match action:
            case "attack":
                if self.weapon:
                    return f"{self.weapon}  {self.name} attacks {player2.name} and deals {damage} HP damage."
                return f"🤜 {self.name} attacks {player2.name} and deals {damage} HP damage."
            case 'kills':
                return f"💀 {self.name} kills {player2.name}!"
            case 'reflected':
                return f"🥴 {self.name} attacks {player2.name} but the attack is refleted, he deals {damage} HP damage to himself."
            case 'critical':
                return f"💥 {self.name} attacks {player2.name} and deals fatality {damage} HP damage."
            case 'heal':
                return f"💉 {self.name} heals {player2.name} and restores {damage} HP."
            case 'critical_heal':
                return f"🚑 {self.name} heals {player2.name} and restores critical {damage} HP."
            case 'heal_reflected':
                return f"🩹 {self.name} tries to heal {player2.name} but the heal is reflected, he deals {damage} HP damage to himself."

            case _:
                return "Invalid action"

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

        if other_team.get_tank() and other_team.get_tank().is_alive():
            enemy = other_team.get_tank()
        else:
            enemy = random.choice(alive_enemies)

        # 5% chance to deal 20 HP damage
        if random.random() < 0.05:
            damage = 20
            if self.weapon:
                damage = self.weapon.new_damage(damage)
            enemy.hp -= damage
            if enemy.hp <= 0:
                enemy.hp = 0
                return self.action_lib(enemy, damage, 'kills')

            return self.action_lib(enemy, damage, 'critical')

        # 5% chance for the attack to be reflected back
        if random.random() < 0.05:
            damage = random.randint(1, 10)
            if self.weapon:
                damage = self.weapon.new_damage(damage)
            self.hp -= damage
            if self.hp <= 0:
                self.hp = 0
                return self.action_lib(enemy, damage, 'kills')

            return self.action_lib(enemy, damage, 'reflected')

        # Normal attack
        damage = random.randint(1, 10)
        if self.weapon:
            damage = self.weapon.new_damage(damage)
        enemy.hp -= damage
        if enemy.hp <= 0:
            enemy.hp = 0
            return self.action_lib(enemy, damage, 'kills')

        return self.action_lib(enemy, damage, 'attack')



    def heal_random_ally(self, team):

        alive_allies = [
            ally for ally in team.characters if ally.is_alive() and ally.get_hp() < ally.original_hp]
        
        if self in alive_allies:
            alive_allies.remove(self)
        
        if not alive_allies:
            return None



        ally = random.choice(alive_allies)

        # 5% chance to heal 20 HP damage
        if random.random() < 0.05:
            heal = 20
            ally.hp += heal
            if ally.hp > ally.original_hp:
                ally.hp = ally.original_hp
            return self.action_lib(ally, heal, 'critical_heal')

        # 5% chance for the attack to be reflected back
        if random.random() < 0.05:
            damage = random.randint(1, 10)
            self.hp -= damage
            if self.hp <= 0:
                self.hp = 0
                return self.action_lib(ally, damage, 'kills')
            return self.action_lib(ally, damage, 'heal_reflected')

        # Normal heal
        heal = random.randint(1, 10)
        ally.hp += heal
        if ally.hp > ally.original_hp:
                ally.hp = ally.original_hp
        return self.action_lib(ally, heal, 'heal')

