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
