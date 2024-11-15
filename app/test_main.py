import unittest
from app.classes.Character import Character
from app.classes.Team import Team
from app.main import display_team
from io import StringIO
import sys

class TestMain(unittest.TestCase):

    def setUp(self):
        # Create characters
        self.character1 = Character("Alice", 10, 100)
        self.character2 = Character("Bob", 5, 100)
        self.character3 = Character("Charlie", 2, 100)
        self.character4 = Character("David", 9, 100)
        self.character5 = Character("Eve", 4, 100)
        self.character6 = Character("Frank", 6, 100)

        # Create teams and add characters
        self.team1 = Team("Equipe 1")
        self.team1.add_character(self.character1)
        self.team1.add_character(self.character2)
        self.team1.add_character(self.character3)

        self.team2 = Team("Equipe 2")
        self.team2.add_character(self.character4)
        self.team2.add_character(self.character5)
        self.team2.add_character(self.character6)

    def test_team1_characters(self):
        characters = self.team1.get_characters()
        self.assertEqual(len(characters), 3)
        self.assertIn(self.character1, characters)
        self.assertIn(self.character2, characters)
        self.assertIn(self.character3, characters)

    def test_team2_characters(self):
        characters = self.team2.get_characters()
        self.assertEqual(len(characters), 3)
        self.assertIn(self.character4, characters)
        self.assertIn(self.character5, characters)
        self.assertIn(self.character6, characters)

    def test_display_team(self):
        # Capture the output of display_team function

        captured_output = StringIO()
        sys.stdout = captured_output
        display_team(self.team1)
        sys.stdout = sys.__stdout__

        output = captured_output.getvalue()
        self.assertIn("Team name: Equipe 1", output)
        self.assertIn("Alice", output)
        self.assertIn("Bob", output)
        self.assertIn("Charlie", output)

if __name__ == '__main__':
    unittest.main()