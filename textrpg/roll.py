from random import randrange
from combat import monster 

# Randomly rolls and executes an event
def roll(hp, attack, steps):
    roll = randrange(0,100)

    if 0 <= roll <= 20:
        print("You carefully move a step forward...")
        steps += 1
        print("You advanced a step forward, you made %s steps so far!" %steps)
        
    elif 21 <= roll <= 40:
        print("You feel a surge of energy as you press forth!")
        steps += 3
        print("You advanced 3 steps forward, you made %s steps so far!" %steps)

    elif 41<= roll <= 45:
        print("You feel delusional from the fatigue, sleep for the night.")
        print("You decided to take a rest for the night,  you made %s steps so far!" %steps)

    elif 46 <= roll <= 50:
        print("You got poisoned by a goblin! You have no choice but to retreat for now")
        steps-=2
        print("You had no choice but to retreat 2 steps,  you made %s steps so far!" %steps)

    elif 51 <= roll <= 60:
        print("You have been blessed by a cleric!")
        hp += 25
        print("Your hp has been restored by 25 points, you now have %s health!" % hp)

    elif 61 <= roll <= 65:
        print("You picked up a magical rune. You feel the surge of power coursing through you!")
        attack *= 2
        print("Your attack doubled in damage, you now have %s attack!" % attack)

    else:
        hp, attack, steps = monster(hp, attack, steps)

    return hp,attack,steps