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

def display_heal_bar(character):
    score = int(character.hp / character.original_hp * 100)
    if score >= 75:
        heart = "💚"
    elif score >= 50:
        heart = "💛"
    elif score >= 25:
        heart = "🧡"
    else:
        heart = "❤️"
    return f"[{"█" * score}] {heart}"


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
        if character == team.get_tank():
            name = f"{character.name} 🎯"
            name = name.ljust(14)
        elif character == team.get_healer():
            name = f"{character.name} 🩺"
            name = name.ljust(14)
        else:    
            name = character.name
            name = name.ljust(15)
        speed = str(character.speed).ljust(3)
        if character.weapon:
            name = str(character.weapon) + "  " + name
        else:
            name = "   " + name
        if character.shield:
            name = "🛡️ " + name
        else:
            name = "  " + name

        if character.is_alive():
            print(f"{name} ⚡️{speed} {display_heal_bar(character)}")
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
    print()
    print()
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
