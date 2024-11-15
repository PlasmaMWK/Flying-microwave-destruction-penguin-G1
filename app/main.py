from classes.Character import Character
from classes.Team import Team
from app.View.display_manager import display_team, display_for_each_round



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
display_for_each_round(team1, team2)