import random
import time
import os


def clear_console():
    if os.name == 'nt':  # Pour Windows
        os.system('cls')
    else:  # Pour macOS et Linux
        os.system('clear')



def display(text):
    print(text)

def display_attack(label):
    print(f"  {label}")


def display_team(team):
    if not team.is_alive():
        display(f"\t-- {team.name} --")
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
            print(f"{name} {speed} [{"█" * character.get_hp()}] HP: {character.get_hp()}")
            print()
        else:
            display(f"{name} {speed} 🪦")
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

    print()
    print()
    print(f"\t-- {team.name} WIN --")
    print()
