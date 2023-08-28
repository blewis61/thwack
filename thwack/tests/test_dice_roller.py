import unittest
from lib import dice_roller


class DiceRollerTest(unittest.TestCase):
    def test_dice_has_allowed_number_of_sides(self):
        self.assertEqual(
            dice_roller.DICE_TYPES,
            ("d4", "d6", "d8", "d10", "d12", "d20", "d100")
        )

    def test_roll(self):
        for dice in dice_roller.DICE_TYPES:
            sides = int(dice[1:])
            result = dice_roller.dice_roll(1, dice)
            self.assertTrue(1 <= result <= sides) 

    def test_total_roll(self):
        result = dice_roller.dice_roll(2, "d4")
        self.assertTrue(2 <= result <= 8)
