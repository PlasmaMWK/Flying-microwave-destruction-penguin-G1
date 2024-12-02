import unittest
from classes.Team import Team
from classes.Character import Character


class TestTeam(unittest.TestCase):
    def test_get_name(self):
        team = Team("Team")

        self.assertEqual("Team", team.get_name())

    def test_get_hp(self):
        team = Team("Team")

        team.add_character(Character("Alex", speed=5))
        team.add_character(Character("Kevin", speed=7))

        self.assertEqual(200, team.get_hp())

    def test_is_alive(self):
        team = Team("Team")

        team.add_character(Character("Alex", speed=5))
        team.add_character(Character("Kevin", speed=7))

        self.assertTrue(team.is_alive())

    def test_is_dead(self):
        team = Team("Team")

        team.add_character(Character("Alex", speed=5))
        team.add_character(Character("Kevin", speed=7))

        self.assertFalse(team.is_dead())


if __name__ == '__main__':
    unittest.main()
