import random
import time
import os


def clear_console():
    if os.name == 'nt':  # Pour Windows
        os.system('cls')
    else:  # Pour macOS et Linux
        os.system('clear')


def display_blinking_text(text):
    print(f"\033[5;92m{text}\033[0m")


def display_red_text(text):
    print(f"\033[31m{text}\033[0m")


def display_green_text(text):
    print(f"\033[92m{text}\033[0m")


def display_attack(label):
    if label:
        print(f"  {label}")


def display_team(team):
    if not team.is_alive():
        display_red_text(f"\t-- {team.name} --")
    else:
        print(f"\t-- {team.name} --")
    print()

    characters = team.get_characters()
    if characters is None:
        characters = []

    characters.sort(key=lambda x: x.speed, reverse=True)

    for character in characters:
        name = character.name.ljust(15)
        speed = str(character.speed).ljust(3)

        if character.is_alive():
            print(f"{name} ⚡️{speed} [{"█" * character.get_hp()}] ❤️")
            print()
        else:
            display_red_text(f"{name} ⚡️{speed} 🪦")
            print()
    print()


def display_teams(team1, team2):
    print()
    display_team(team1)
    print()
    display_team(team2)
    print()


def display_for_each_round(team1, team2, round_nb=0):
    clear_console()
    display_teams(team1, team2)
    print(f"\t**** Round {round_nb} ****")
    print(f"\t------------------")
    print()


def display_winner(team):

    display_blinking_text(f"  ***********************************")
    display_blinking_text(f"  *         Congrats {team.name.ljust(15)}*")
    display_blinking_text(f"  *            YOU WIN 🏆           *")
    display_blinking_text(f"  ***********************************")
    print()
    

def display_logs(logs):
    print()
    round_number = 1
    for round_logs in logs:
        display_green_text(f"\t**** Round {round_number} ****")
        for log in round_logs:
            display_attack(log)
        round_number += 1
        print()
