#remember to save and test your code often
#https://trinket.io/python/e5a03e7cbc
#https://coding-grace-guide.readthedocs.io/en/latest/guide/lessonplans/beginners-python-text-based-adventure.html
print("\n THAD'S SCI-FI MYSTERY GAME!")
print('\n Once you start playing, you will be asked questions throughout the game. You will have two options for each question, and you must enter "1" or "2" to select your answer.')
print('\n Typing "1" will select the first option, and typing "2" will select the second option.')

print('\n .........')
print()

def initial_game():
    print('You awake in an unfamiliar place. After glancing around, you determine that you are most likely in the cargo deck of a spaceship.')
    first_q = input('Option 1: Leave the cargo deck through the main door. Option 2: Leave the cargo deck by climbing the ladder to the hatch. ')
    if first_q == '1':
        def door_game():
            print('\n You open the main door and enter a dimly lit hallway. There is a being in the shadows that threatens your safety.')
            door_q = input('Option 1: Attempt to fight the creature. Option 2: Run away towards the stairs.')
            if door_q == '1':
                print('\n You try to fight, but the creature unfortunetly eats you. END OF GAME.')
                quit()
            elif door_q == '2':
                print('\n You manage to escape from the creature. You have reached another hallway with two doors.')
                runaway_q = input('Option 1: You head through the door labeled "DOCKING BAY". Option 2: You head through the door labeled "ARMORY."')
                if runaway_q == '1':
                    print('\n Upon entering the docking bay, you see that there is a massive spacecraft docked onto the ship. Sentient creatures with human-sized mouths proceed to capture and eat you. GAME OVER.')
                    quit()
                elif runaway_q == '2':
                    print('\n Upon entering the armory, you instinctively grab a few weapons from the walls. Shortly after, hundreds of creatures (like the one you ran away from) begin to charge you. The high tech weapons allow you to fight your way to an escape pod and you safely escape. END OF GAME.')
                    quit()
            else:
                print('\n Invalid response. Try again.')
                door_game()
        door_game()
    elif first_q == '2':
        def ladder_game():
            print('\n You climb the ladder and go through the hatch. You appear to be in the living quarters.')
            hatch_q = input('Option 1: You explore the living quarters in hope of finding any information. Option 2: Feeling tired, you decide to take a nap on one of the beds.')
            if hatch_q == '1':
                def quarters_game():
                    print('\n After looking around, you find a hologram message near one of the beds. The hologram shows a shipmate explaining that an unknown pirate spacecraft has docked onto the ship you are currently in. The hologram cuts out suddenly.')
                    hologram_q = input('Option 1: You head to the restroom to use the toilet. Option 2: You take the elavator up to the top of the ship.')
                    if hologram_q == '1':
                        print('\n Upon using the toilet, a creature crawls out of the toilet and eats you. GAME OVER.')
                        quit()
                    elif hologram_q == '2':
                        def hologram_game():
                            print('\n After reaching the top of the ship, you are face to face with the cockpit doors and the escape pods.')
                            final_q = input('Option 1: You head into the cockpit. Option 2: You take an escape pod and leave the ship.')
                            if final_q == '1':
                                print('\n You enter the cockpit and find the full security feed. You watch the tapes as you discover that an alien pirate ship has come to pillage your ship. Your memories come flooding back as you are eaten by one of the aliens. GAME OVER.')
                                quit()
                            elif final_q == '2':
                                print('\n You take an escape pod and sucessfully escape from the ships. Yet, you wonder what really happened there. END OF GAME.')
                                quit()
                            else:
                                print('\n Invalid response. Try again.')
                                hologram_game()
                        hologram_game()
                    else:
                        print('\n Invalid response. Try again.')
                        quarters_game()
                quarters_game()
            elif hatch_q == '2':
                print('\n While sleeping, you are eaten, END OF GAME.')
                quit()
            else:
                print('\n Invalid response. Try again.')
                ladder_game()
        ladder_game()
    else:
        print('\n Invalid response. Try again.')
        initial_game()
initial_game()