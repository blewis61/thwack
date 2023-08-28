import unittest
from lib import fighter
from unittest.mock import MagicMock

class TestFighter(unittest.TestCase):
    def test_attack_rating_between_1_to_20(self):
        test_fighter = fighter.Fighter("Fighter 1")
        self.assertIn(
            test_fighter.attack_rating,
            range(1, 21)
        )

    def test_defense_rating_between_1_to_20(self):
        test_fighter = fighter.Fighter("Fighter 1")
        self.assertIn(
            test_fighter.defense_rating,
            range(1, 21)
        )
    
    def test_hit_points_are_100(self):
        test_fighter = fighter.Fighter("Fighter 1")
        self.assertEqual(
            test_fighter.hit_points,
            100
        )

    def test_attack_higher_attack_rating_wins(self):
        test_attacker = MagicMock()
        test_attacker.attack_rating = 21
        test_defender = MagicMock()
        test_defender.defense_rating = 1
        test_defender.hit_points = 20

        fighter.Fighter.attack(test_attacker, test_defender)
    
        self.assertTrue(
            test_defender.hit_points < 20
        )
        
    def test_attack_higher_defense_rating_wins(self):
        test_attacker = MagicMock()
        test_attacker.attack_rating = 1
        test_defender = MagicMock()
        test_defender.defense_rating = 21
        test_defender.hit_points = 20

        fighter.Fighter.attack(test_attacker, test_defender)
    
        self.assertEqual(test_defender.hit_points, 20)

    def test_attack_does_1_to_10_damage(self):
        test_attacker = MagicMock()
        test_attacker.attack_rating = 21
        test_defender = MagicMock()
        test_defender.defense_rating = 1
        test_defender.hit_points = 20

        fighter.Fighter.attack(test_attacker, test_defender)

        self.assertIn(test_defender.hit_points, range(10, 20))

if __name__ == '__main__':
    unittest.main()