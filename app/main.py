from app.classes.Character import Character
from app.classes.Team import Team


# Function to display the characters in a team
def display_team(team):
    print(f"Team name: {team.name}")
    print("Characters:")
    for character in team.get_characters():
        print(character)




# Create 3 characters
character1 = Character("Alice", 10, 100)
character2 = Character("Bob", 5, 100)
character3 = Character("Charlie", 2, 100)

# Create a team and add the characters
team1 = Team("Equipe 1")
team1.add_character(character1)
team1.add_character(character2)
team1.add_character(character3)

#Create other characters
character4 = Character("David", 9, 100)
character5 = Character("Eve", 4, 100)
character6 = Character("Frank", 6, 100)

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
    while True:
        perform_attack(team1, team2)
        perform_attack(team2, team1)

        # Afficher les équipes après chaque tour
        print("\n--- État des équipes ---")
        display_team(team1)
        display_team(team2)

        # Vérifier si une équipe est entièrement KO
        if not any(character.get_hp() > 0 for character in team1.get_characters()):
            print("L'équipe 2 a gagné !")
            break
        if not any(character.get_hp() > 0 for character in team2.get_characters()):
            print("L'équipe 1 a gagné !")
            break
