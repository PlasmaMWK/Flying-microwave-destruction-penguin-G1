import unittest
from classes.Character import Character
from classes.Team import Team
from View.display_manager import display_team, display_for_each_round

class TestMain(unittest.TestCase):
    def setUp(self):
            self.character1 = Character("Alice", 10)
            self.character2 = Character("Bob", 8)
            self.character3 = Character("Charlie", 2)
            self.character4 = Character("David", 9)
            self.character5 = Character("Eve", 4)
            self.character6 = Character("Frank", 6)
            self.team1 = Team("Equipe 1")
            self.team2 = Team("Equipe 2")
            self.team1.add_character(self.character1)
            self.team1.add_character(self.character2)
            self.team1.add_character(self.character3)
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

    def test_attack_random_enemy_no_enemies(self):
            empty_team = Team("Empty Team")
            self.assertIsNone(self.character1.attack_random_enemy(empty_team))

    def test_attack_random_enemy_character_dead(self):
        self.character1.hp = 0
        self.assertIsNone(self.character1.attack_random_enemy(self.team2))

    def test_attack_random_enemy_enemy_dead(self):
        self.character4.hp = 0
        self.character5.hp = 0
        self.character6.hp = 0
        self.assertIsNone(self.character1.attack_random_enemy(self.team2))

    def test_attack_random_enemy(self):
        targets = set()
        for _ in range(100):  # Run the attack multiple times to check randomness
            target = self.character1.attack_random_enemy(self.team2)
            targets.add(target)
        self.assertTrue(len(targets) > 1, "The attack should target different enemies randomly")


if __name__ == '__main__':
    unittest.main()