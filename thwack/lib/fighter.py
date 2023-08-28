from lib import dice_roller
import random

class Fighter():
    def __init__(self, name):
        self.name = name
        self.hit_points = 50
        self.attack_rating = dice_roller.dice_roll(1, "d20")
        self.defense_rating = dice_roller.dice_roll(1, "d20")
        print(f"{self.name} has an attack rating of {self.attack_rating} and a defense rating of {self.defense_rating}")

    def attack(self, target):
        attack_attempt = self.attack_rating + dice_roller.dice_roll(1, "d20")
        defense_attempt = target.defense_rating + dice_roller.dice_roll(1, "d20")
        damage = dice_roller.dice_roll(1, "d10")

        LIGHT_ATTACK_MSG = [
            f"{self.name} barely knicks {target.name} causing {damage} damage and reducing {target.name}'s hitpoints to {target.hit_points}.",
            f"{self.name} swings hard but {target.name} dodges at the last moment taking a glancing blow causing {damage} damage and reducing {target.name}'s hitpoints to {target.hit_points}.",
            f"{self.name} hits {target.name} with all the strength of an angry mosquito causing {damage} damage and reducing {target.name}'s hitpoints to {target.hit_points}."
                            ]
        
        STANDARD_ATTACK_MSG = [
            f"{self.name} thwacks {target.name} causing {damage} damage, reducing {target.name}'s hitpoints to {target.hit_points}.", 
            f"{self.name} hits {target.name} solidly across the chest causing {damage} damage, reducing {target.name}'s hitpoints to {target.hit_points}.",
            f"{self.name} pummels {target.name} causing {damage} damage, reducing {target.name}'s hitpoints to {target.hit_points}."
        ]

        HARD_ATTACK_MSG = [
            f"{self.name} slashes hard at {target.name} rending their armor and causing {damage} damage, reducing {target.name}'s hitpoints to {target.hit_points}.",
            f"{self.name} viciously slams their weapon into {target.name} causing {damage} damage and reducing {target.name}'s hitpoints to {target.hit_points}.",
            f"{target.name} attempts to dodge but moves directly into the path of {self.name}'s blow taking {damage} damage and reducing {target.name}'s hitpoints to {target.hit_points}."
        ]

        MAJOR_MISS_MSG = [
            f"{self.name} nearly trips over himself trying to hit {target.name}, missing badly and barely staying on their feet.",
            f"{self.name} swings with all their might but drops their sword! It's a good thing {target.name} was laughing so hard, giving {self.name} a chance to pick up their weapon.",
            f"{self.name} steps toward {target.name} to attack but {target.name} dances quickly out of the way, slapping {self.name} hard across the backside with the flat of their blade. The shame!"
        ]

        STANDARD_MISS_MSG = [
            f"{target.name} moves raises their shield and blocks the attack by {self.name}",
            f"{target.name}'s blade catches {self.name}'s sword and deflects it harmlessly away.",
            f"{target.name} spins to the right as {self.name}'s weapon slashes the air where they stood moments before."
        ]

        CLOSE_MISS_MSG = [
            f"{target.name} raises their shield at the last moment, barely catching {self.name}'s blade.",
            f"{target.name} steps back as {self.name}'s blade slashes toward their stomach - the blade slices through {target.name}'s shirt, but fails to make contact.",
            f"{self.name} strikes viciously at {target.name}'s head. {target.name} ducks just in time - hope he wanted that haircut."
        ]

        if attack_attempt > defense_attempt:
            target.hit_points -= damage
            
            if damage <= 3:
                print(random.choice(LIGHT_ATTACK_MSG))
            elif damage >= 4 <= 8:
                print(random.choice(STANDARD_ATTACK_MSG))
            else:
                print(random.choice(HARD_ATTACK_MSG))

        else:
            if defense_attempt - attack_attempt <= 5:
                print(random.choice(CLOSE_MISS_MSG))

            elif defense_attempt - attack_attempt > 5 <= 15:
                print(random.choice(STANDARD_MISS_MSG))
            
            else:
                print(random.choice(MAJOR_MISS_MSG))
