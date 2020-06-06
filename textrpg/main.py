from roll import roll

hp = 1
attack = 5
game_status = 0
steps = 0


while hp > 0:

    choice = int(input("What would you like to do now traveller? \n1)Press on!\n2)Check hp\n3)Check attack\n4)Check steps\n"))

    if choice == 1:
        hp,attack,steps = roll(hp,attack,steps)
    elif choice == 2:
        print("You now have %2s hp!" %hp)
    elif choice == 3:
        print("You now have %s attack!" %attack)
    elif choice == 4:
        print("You have moved %s steps so far!" %steps)
    
    print("=============================================")


