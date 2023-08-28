from lib import fighter
import time

fighter_1 = fighter.Fighter("Fighter 1")
fighter_2 = fighter.Fighter("Fighter 2")

def play_thwack():
    fight_round = 1

    while fighter_1.hit_points > 0 and fighter_2.hit_points > 0:
        fighter_1.attack(fighter_2)
        fighter_2.attack(fighter_1)

        if fighter_1.hit_points <= 0:
            print("Fighter 1 has fallen! Fighter 2 is victorious")
            break
        
        if fighter_2.hit_points <= 0:
            print("Fighter 2 has fallen! Fighter 1 is victorious")
            break

        print(f"After round {fight_round} {fighter_1.name} has {fighter_1.hit_points} hit points remaining and {fighter_2.name} has {fighter_2.hit_points} hitpoints remaining.")
        fight_round += 1

        if fighter_1.hit_points > 0 and fighter_2.hit_points > 0:
            print("Simulating next round . . .")
            time.sleep(3)

play_thwack()