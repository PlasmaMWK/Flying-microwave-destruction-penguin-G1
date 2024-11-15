from classes.Character import Character
from classes.Team import Team
from View.display_manager import display_team, display_for_each_round
import random



# Create 3 characters
character1 = Character("Alice", 10)
character2 = Character("Bob", 5)
character3 = Character("Charlie", 2)

# Create a team and add the characters
team1 = Team("Equipe 1")
team1.add_character(character1)
team1.add_character(character2)
team1.add_character(character3)

#Create other characters
character4 = Character("David", 9)
character5 = Character("Eve", 4)
character6 = Character("Frank", 6)

# Create an other team and add the characters
team2 = Team("Equipe 2")
team2.add_character(character4)
team2.add_character(character5)
team2.add_character(character6)

    
# Display the characters in the teams
display_team(team1)
display_team(team2)

def game_loop(team1, team2):
    """
    Boucle de jeu où les deux équipes s'affrontent.
    """
    print("\n--- Début du combat ---")
    while team1.get_hp() > 0 and team2.get_hp() > 0:

        # Attaquer un ennemi aléatoire dans chaque équipe
        perform_attack(team1, team2)
        
        if team2.get_hp() > 0:
            perform_attack(team2, team1)

        # Afficher les équipes après chaque tour
        print("\n--- État des équipes ---")
        display_team(team1)
        display_team(team2)

    print("\n--- Fin du combat ---")
    if team1.get_hp() <= 0:
        print(f"L'équipe {team2.get_name()} a gagné. \n ○( ＾皿＾)っ Hehehe…")
    else:
        print(f"L'équipe {team1.get_name()} a gagné. \n ○( ＾皿＾)っ Hehehe…")


def perform_attack(attacking_team, defending_team):
    attacker = random.choice([char for char in attacking_team.get_characters() if char.get_hp() > 0])
    attacker.attack_random_enemy(defending_team)

game_loop(team1, team2)