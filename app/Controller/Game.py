import classes.Team as Team
import classes.Character as Character
import random
import time
import os
from View.display_manager import display_winner, display_for_each_round, clear_console, display_attack


class Game:
    def __init__(self, team1, team2):
        self.team1 = team1
        self.team2 = team2
        self.round_nb = 1
        self.winner = None
        self.loser = None

    def get_winner(self):
        return self.winner

    def perform_attack(self, attacking_team, defending_team):
        # get the attacker with the highest speed and still alive
        attacker = max([char for char in attacking_team.get_characters(
        ) if char.is_alive()], key=lambda x: x.get_speed())

        return attacker.attack_random_enemy(defending_team)

    def round(self, round_nb):
        attack1 = self.perform_attack(self.team1, self.team2)

        if self.team2.is_alive():
            attack2 = self.perform_attack(self.team2, self.team1)
        else:
            attack2 = None

        display_for_each_round(self.team1, self.team2, round_nb)

        display_attack(attack1)
        if attack2:
            display_attack(attack2)
        else:
            print()

        print()

    def start(self):

        while self.team1.is_alive() and self.team2.is_alive():
            time.sleep(0.5)
            self.round(self.round_nb)
            self.round_nb += 1

        if self.team1.is_dead():
            self.winner = self.team2
            self.loser = self.team1
        else:
            self.winner = self.team1
            self.loser = self.team2

        display_winner(self.winner)
