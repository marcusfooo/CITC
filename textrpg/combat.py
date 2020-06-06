from random import choice
from time import sleep


# Combat process
def battle(hp, attack, steps, monster, monsterhp, monsterattack):

    while hp > 0 and monsterhp > 0:
        playerMove = int(input("What would you like to do? \n1)Slash\n2)Energy Burst\n3)Meditate\n"))

        if playerMove == 1:
            print("You swung your blade at the %s" %monster)
            print("%s groans in pain..." %monster)
            print("%s swings at you!" %monster)
            monsterhp -= attack
            hp -= monsterattack

        if playerMove == 2:
            print("Kame...")
            sleep(1)
            print("Kame...")
            sleep(1)
            print("HAAAAAAA!!!")
            sleep(1)
            print("%s groans in pain..." %monster)
            print("%s swings at you!" %monster)
            monsterhp -= attack
            hp -= monsterattack

        if playerMove == 3:
            print("You enter into a meditative state and restored 20 health!")
            hp += 20
            print("%s chuckles..." %monster)
            print("%s swings at you!" %monster)
            monsterhp -= attack
            hp -= monsterattack

    # Exit game if player dies   
    if hp < 0:
        print("You have died an honorable death!")
        exit()

    print("You have slain the %s !" %monster)
    print("You now have %s hp!" %hp)
    print("You moved forward a step!")
    steps += 1
    return hp, attack, steps


# Chooses a monster to fight
def monster(hp, attack, steps, game_status):
    monsterOptions = ["Troll", "Goblin", "Ogre"]
    monster = choice(monsterOptions)

    if steps < 20:
        print("You have encounted a %s !" %monster)
        if monster == "Troll":
            monsterhp = 20
            monsterattack = 4
        elif monster == "Goblin":
            monsterhp = 10
            monsterattack = 6
        elif monster == "Ogre":
            monsterhp = 40
            monsterattack = 5

        hp, attack, steps = battle(hp, attack, steps, monster, monsterhp, monsterattack)
    else:
        print("Foolish human! Face the wrath of the Goblin King!")
        monster = "Goblin King"
        monsterhp = 300
        monsterattack = 15
        hp, attack, steps = battle(hp, attack, steps, monster, monsterhp, monsterattack)

        # If goblin king is slain, update game status
        game_status = 1

    return hp, attack, steps, game_status