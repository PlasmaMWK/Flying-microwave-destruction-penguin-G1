import unittest
from classes.Team import Team
from classes.Character import Character


class TestCharacter(unittest.TestCase):
    def test_get_name(self):
        char = Character("Toto", speed=5)

        self.assertEqual("Toto", char.get_name())

    def test_get_speed(self):
        char = Character("Toto", speed=5)

        self.assertEqual(5, char.get_speed())

    def test_get_hp(self):
        char = Character("Toto", speed=5)

        self.assertEqual(100, char.get_hp())

    def test_is_alive(self):
        char = Character("Toto", speed=5)

        self.assertTrue(char.is_alive())

    def test_is_dead(self):
        char = Character("Toto", speed=5)

        self.assertFalse(char.is_dead())


if __name__ == '__main__':
    unittest.main()
