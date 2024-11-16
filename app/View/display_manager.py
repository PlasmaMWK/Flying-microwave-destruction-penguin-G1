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
    print(label)


def display_team(team):
    if not team.get_is_alive():
        display_red_text(f"-- {team.name} --")
    else:
        print(f"-- {team.name} --")

    characters = team.get_characters()
    if characters is None:
        characters = []

    characters.sort(key=lambda x: x.speed, reverse=True)

    for character in characters:
        name = character.name.ljust(15)
        speed = str(character.speed).ljust(3)

        if character.is_alive():
            print(f"{name} ⚡️{speed} ❤️ {"|" * character.get_hp()}")
        else:
            display_red_text(f"{name} ⚡️{speed} 🪦")
    print()


def display_teams(team1, team2):
    display_team(team1)
    display_team(team2)


def display_for_each_round(team1, team2, round_nb=0):
    clear_console()
    print(f"\t\t **** Round {round_nb} ****")

    display_teams(team1, team2)


def display_winner(team):

    display_blinking_text(f"***********************************")
    display_blinking_text(f"*         Congrats {team.name.ljust(15)}*")
    display_blinking_text(f"*            YOU WIN 🏆           *")
    display_blinking_text(f"***********************************")
    print()
