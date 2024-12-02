import time
from View.display_manager import display_winner, display_for_each_round, display_attack


class Game:
    def __init__(self, team1, team2):
        self.team1 = team1
        self.team2 = team2
        self.round_nb = 1
        self.winner = None
        self.loser = None
        self.log = []

    def get_winner(self):
        return self.winner

    def perform_attack(self, attacking_team, defending_team):
        # get the attacker with the highest speed and still alive
        attacker = max([char for char in attacking_team.get_characters(
        ) if char.is_alive()], key=lambda x: x.get_speed())

        return attacker.attack_random_enemy(defending_team)

    def round(self, round_nb):
        attackList = []
        combined_team = self.team1.get_characters() + self.team2.get_characters()
        combined_team.sort(key=lambda x: x.get_speed(), reverse=True)


        for player in combined_team:
            if player.is_alive():
                if player in self.team1.get_characters():
                    attackList.append(player.attack_random_enemy(self.team2))
                else:
                    attackList.append(player.attack_random_enemy(self.team1))

        display_for_each_round(self.team1, self.team2, round_nb)

        for attack in attackList:
            if attack:
                display_attack(attack)
        return attackList


    def start(self):
        while self.team1.is_alive() and self.team2.is_alive():
            time.sleep(1)
            self.log = []

            self.log.append({
                'round': self.round_nb,
                'attacks': self.round(self.round_nb)
            })
            self.round_nb += 1

        if self.team1.is_dead():
            self.winner = self.team2
            self.loser = self.team1
        else:
            self.winner = self.team1
            self.loser = self.team2

        display_winner(self.winner)
        
