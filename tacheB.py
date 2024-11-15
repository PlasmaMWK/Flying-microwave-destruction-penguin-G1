import random

class Character:
    def __init__(self, name):
        self.name = name
        self.hp = 100  # Points de vie par défaut

    def is_alive(self):
        return self.hp > 0

    def attack(self, target):
        if not self.is_alive():
            print(f"{self.name} est KO et ne peut pas attaquer.")
            return
        damage = random.randint(1, 10)  # Dégâts aléatoires entre 1 et 10
        target.hp -= damage
        print(f"{self.name} attaque {target.name} et inflige {damage} HP !")
        if target.hp <= 0:
            print(f"{target.name} est KO !")


def perform_attack(attacking_team, defending_team):
    """
    Gère une attaque aléatoire d'un joueur vivant de l'équipe attaquante 
    contre un joueur vivant de l'équipe défendante.
    """
    # Filtrer les joueurs vivants dans les deux équipes
    attackers = [char for char in attacking_team if char.is_alive()]
    defenders = [char for char in defending_team if char.is_alive()]

    if not attackers or not defenders:
        return  # Aucune attaque possible si l'une des équipes n'a plus de joueurs vivants

    attacker = random.choice(attackers)  # Choisir un attaquant vivant
    target = random.choice(defenders)  # Choisir une cible vivante
    attacker.attack(target)

def main():
    # Créer deux équipes
    team1 = [Character(f"Team1_Player{i+1}") for i in range(3)]
    team2 = [Character(f"Team2_Player{i+1}") for i in range(3)]

    # Afficher les équipes initiales
    print("\n--- Début du combat ---")
    for char in team1 + team2:
        print(f"{char.name}: {char.hp} HP")

    # Simuler une attaque
    print("\n--- Simulation d'une attaque ---")
    perform_attack(team1, team2)

if __name__ == "__main__":
    main()
