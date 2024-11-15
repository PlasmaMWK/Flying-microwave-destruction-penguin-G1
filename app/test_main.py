import unittest
from unittest.mock import patch, MagicMock
from classes.Character import Character
from classes.Team import Team
from main import game_loop, perform_attack

class TestGame(unittest.TestCase):

    def setUp(self):
        # Create characters
        self.character1 = Character("Alice", 10)
        self.character2 = Character("Bob", 5)
        self.character3 = Character("Charlie", 2)
        self.character4 = Character("David", 9)
        self.character5 = Character("Eve", 4)
        self.character6 = Character("Frank", 6)

        # Create teams and add characters
        self.team1 = Team("Equipe 1")
        self.team1.add_character(self.character1)
        self.team1.add_character(self.character2)
        self.team1.add_character(self.character3)

        self.team2 = Team("Equipe 2")
        self.team2.add_character(self.character4)
        self.team2.add_character(self.character5)
        self.team2.add_character(self.character6)

    @patch('main.display_team')
    def test_game_loop(self, mock_display_team):
        with patch('main.perform_attack') as mock_perform_attack:
            mock_perform_attack.side_effect = self.mock_perform_attack
            game_loop(self.team1, self.team2)
            self.assertTrue(mock_perform_attack.called)

    def mock_perform_attack(self, attacking_team, defending_team):
        for character in defending_team.get_characters():
            character.hp = 0

    @patch('random.choice')
    def test_perform_attack(self, mock_random_choice):
        mock_random_choice.return_value = self.character1
        self.character1.attack_random_enemy = MagicMock()
        perform_attack(self.team1, self.team2)
        self.character1.attack_random_enemy.assert_called_once_with(self.team2)

if __name__ == '__main__':
    unittest.main()