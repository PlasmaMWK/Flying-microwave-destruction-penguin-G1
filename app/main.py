from classes.Character import Character
from classes.Team import Team
from Controller.Game import Game
from classes.Weapon import Weapon

from View.display_manager import display_teams, clear_console, display_logs

def create_team(team_name,nb_team):
    team = Team(team_name)
    for i in range(nb_team):
        print(team_name)
        print("-------")
        name = input(f"Enter the name of the player {i+1} :")
        speed = int(input(f"Enter the speed of {name} :"))
        stamina = int(input(f"Enter the stamina of {name} :"))
        weapon = input(f"Is {name} have a weapon ? y/n :")
        shield = input(f"Is {name} have a shield ? y/n :")
        name = f"{i+1} - {name}"
        team.add_character(Character(name, speed=speed, stamina=stamina, weapon=Weapon() if weapon == "y" else None, shield=True if shield == "y" else False))
        clear_console()
    
    
    return team


# Create a team and add the characters
clear_console()
nb_team = int(input("How many players per team :"))
team1_name = input("Enter the name of the first team :")
team2_name = input("Enter the name of the second team :")
clear_console()
team1 = create_team(team1_name,nb_team)
team2 = create_team(team2_name,nb_team)


def player_class(team):
    tank = input(f"Who is the tank of {team.name} ? (number) :")
    healer = input(f"Who is the healer of {team.name} ? (number) :")
    if tank and tank != "":
        tank = int(tank)
        if tank <= len(team.characters) and tank > 0:
            team.tank = team.characters[tank-1]
    if healer and healer != "":
        healer = int(healer)
        if healer <= len(team.characters) and healer > 0:
            team.healer = team.characters[healer-1]

    return team

game = Game(team1, team2)

# Display the teams
clear_console()
display_teams(team1, team2)
team1 = player_class(team1)
team2 = player_class(team2)
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
