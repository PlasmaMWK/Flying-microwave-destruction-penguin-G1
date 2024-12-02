from classes.Character import Character
from classes.Team import Team
from Controller.Game import Game

from View.display_manager import display_teams, clear_console, display_logs

# Create a team and add the characters
team1 = Team("Team 1")
team1.add_character(Character("Alex", speed=5))
team1.add_character(Character("Kevin", speed=7))
team1.add_character(Character("Aymeric", speed=10))
team1.add_character(Character("Chris", speed=6))
team1.add_character(Character("Youness", speed=6))

# Create an other team and add the characters
team2 = Team("Team 2")
team2.add_character(Character("Lea", speed=10))
team2.add_character(Character("Théo", speed=6))
team2.add_character(Character("Wilfried", speed=1))
team2.add_character(Character("Zakaria", speed=3))
team2.add_character(Character("Alexis", speed=2))

game = Game(team1, team2)

# Display the teams
clear_console()
display_teams(team1, team2)

start_txt = " Start the game? Press Enter to continue..."
input(f"\033[5;92m{start_txt}\033[0m")
logs = game.start()
input("Press Enter to display the logs of the current game...")
display_logs(logs)
