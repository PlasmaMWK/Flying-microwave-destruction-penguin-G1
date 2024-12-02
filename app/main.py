from classes.Character import Character
from classes.Team import Team
from Controller.Game import Game

from View.display_manager import display_teams, clear_console, display_logs

# Create a team and add the characters
team1 = Team("Team 1")
team1.add_character(Character("Alex", speed=5, stamina=4))
team1.add_character(Character("Kevin", speed=7, stamina=10), tank=True)
team1.add_character(Character("Aymeric", speed=10, stamina=8))
team1.add_character(Character("Chris", speed=6, stamina=9))
team1.add_character(Character("Youness", speed=6, stamina=3), healer=True)

# Create an other team and add the characters
team2 = Team("Team 2")
team2.add_character(Character("Lea", speed=10, stamina=4))
team2.add_character(Character("Théo", speed=6, stamina=5))
team2.add_character(Character("Wilfried", speed=1, stamina=8), tank=True)
team2.add_character(Character("Zakaria", speed=3, stamina=1))
team2.add_character(Character("Alexis", speed=2, stamina=2), healer=True)   

game = Game(team1, team2)

# Display the teams
clear_console()
display_teams(team1, team2)

start_txt = " Start the game? Press Enter to continue..."
log_txt = "Press Enter to display the logs of the current game..."

input(f"\033[5;93m{start_txt}\033[0m")
logs = game.start()
print()
input(f"\033[5;93m{log_txt}\033[0m")
clear_console()

display_logs(logs)
