import random
import time
import os

def clear_console():
    if os.name == 'nt':  # Pour Windows
        os.system('cls')
    else:  # Pour macOS et Linux
        os.system('clear')

# Function to display the characters in a team
def display_team(team):
    print(f"Team name: {team.name}")
    print("Characters:")
    for character in team.get_characters():
        print(character)


# Function to display the characters and their stats in a team for each round
def display_for_each_round(team1, team2):
    i = 1
    while team1.is_alive() and team2.is_alive():
        print(f"Round {i+1} :")
        team1.attack(team2)
        display_team(team2)
        team2.attack(team1)
        display_team(team1)
        i+=1

def game_loop(team1, team2):
    """
    Boucle de jeu où les deux équipes s'affrontent.
    """
    print("\n--- Début du combat ---")
    round = 0
    while team1.get_hp() > 0 and team2.get_hp() > 0:
        round += 1
        # Attaquer un ennemi aléatoire dans chaque équipe
        print(f"\n--- Round {round} ---")
        perform_attack(team1, team2)

        if team2.get_hp() > 0:
            perform_attack(team2, team1)
            # Afficher les équipes après chaque tour
            time.sleep(0.4)
        clear_console()

    print("\n--- Fin du combat ---")
    if team1.get_hp() <= 0:
        print('''\033[92m
              


 _____                      ____             _         _ 
|_   _|__  __ _ _ __ ___   |___ \  __      _(_)_ __   | |
  | |/ _ \/ _` | '_ ` _ \    __) | \ \ /\ / / | '_ \  | |
  | |  __/ (_| | | | | | |  / __/   \ V  V /| | | | | |_|
  |_|\___|\__,_|_| |_| |_| |_____|   \_/\_/ |_|_| |_| (_)
\033[0m''')
    else:
        print('''\033[92m
              

              
 _____                      _            _         _ 
|_   _|__  __ _ _ __ ___   / | __      _(_)_ __   | |
  | |/ _ \/ _` | '_ ` _ \  | | \ \ /\ / / | '_ \  | |
  | |  __/ (_| | | | | | | | |  \ V  V /| | | | | |_|
  |_|\___|\__,_|_| |_| |_| |_|   \_/\_/ |_|_| |_| (_)
\033[0m''')

def perform_attack(attacking_team, defending_team):
    attacker = random.choice([char for char in attacking_team.get_characters() if char.get_hp() > 0])
    attacker.attack_random_enemy(defending_team)
