import unittest
from app.classes.Character import Character
from app.classes.Team import Team
from app.View.display_manager import display_team, display_for_each_round

class TestMain(unittest.TestCase):
    def setUp(self):
        # Create characters for team 1
        self.character1 = Character("Alice", 10, 100)
        self.character2 = Character("Bob", 5, 100)
        self.character3 = Character("Charlie", 2, 100)

        # Create team 1 and add characters
        self.team1 = Team("Equipe 1")
        self.team1.add_character(self.character1)
        self.team1.add_character(self.character2)
        self.team1.add_character(self.character3)

        # Create characters for team 2
        self.character4 = Character("David", 9, 100)
        self.character5 = Character("Eve", 4, 100)
        self.character6 = Character("Frank", 6, 100)

        # Create team 2 and add characters
        self.team2 = Team("Equipe 2")
        self.team2.add_character(self.character4)
        self.team2.add_character(self.character5)
        self.team2.add_character(self.character6)

    def test_team1_characters(self):
        self.assertEqual(len(self.team1.characters), 3)
        self.assertIn(self.character1, self.team1.characters)
        self.assertIn(self.character2, self.team1.characters)
        self.assertIn(self.character3, self.team1.characters)

    def test_team2_characters(self):
        self.assertEqual(len(self.team2.characters), 3)
        self.assertIn(self.character4, self.team2.characters)
        self.assertIn(self.character5, self.team2.characters)
        self.assertIn(self.character6, self.team2.characters)

    def test_display_team(self):
        # Assuming display_team returns a string for testing purposes
        output1 = display_team(self.team1)
        output2 = display_team(self.team2)
        self.assertIn("Alice", output1)
        self.assertIn("Bob", output1)
        self.assertIn("Charlie", output1)
        self.assertIn("David", output2)
        self.assertIn("Eve", output2)
        self.assertIn("Frank", output2)

    def test_display_for_each_round(self):
        # Assuming display_for_each_round returns a string for testing purposes
        output = display_for_each_round(self.team1, self.team2)
        self.assertIn("Equipe 1", output)
        self.assertIn("Equipe 2", output)

if __name__ == '__main__':
    unittest.main()