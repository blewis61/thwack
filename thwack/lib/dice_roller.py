import random

DICE_TYPES = ("d4", "d6", "d8", "d10", "d12", "d20", "d100")

def dice_roll(number_of_dice, type_of_dice):
    """Rolls selected number and type of dice and returns string to user."""
    if type_of_dice not in DICE_TYPES:
        raise ValueError(f"Dice selected is not valid. Dice must be one of the following, {DICE_TYPES}")
    sides = int(type_of_dice[1:])
    roll = random.randint(1, sides)
    total_roll = roll * number_of_dice
    return total_roll

