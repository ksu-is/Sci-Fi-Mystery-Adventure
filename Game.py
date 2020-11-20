#remember to save and test your code often
#https://trinket.io/python/e5a03e7cbc
#https://coding-grace-guide.readthedocs.io/en/latest/guide/lessonplans/beginners-python-text-based-adventure.html
print("\n THAD'S SCI-FI MYSTERY GAME!")
print('\n Once you start playing, you will be asked questions throughout the game. You will have two options for each question, and you must enter "1" or "2" to select your answer.')
print('\n Typing "1" will select the first option, and typing "2" will select the second option.')

print('\n .........')
print()

print('You awake in an unfamiliar place. After glancing around, you determine that you are most likely in the cargo deck of a spaceship.')
first_q = input('Option 1: Leave the cargo deck through the main door. Option 2: Leave the cargo deck by climbing the ladder to the hatch. ')
while True:
    if first_q == '1':
        print('\n You open the main door and enter a dimly lit hallway. There is a being in the shadows that threatens your safety.')
        door_q = input('Option 1: Attempt to fight the creature. Option 2: Run away towards the stairs.')
        while True:
            if door_q == '1':
                print('\n You try to fight, but the creature unfortunetly eats you. END OF GAME.')
                break
            elif door_q == '2':
                print('\n You manage to escape from the creature. You have reached another hallway with two doors.')
    elif first_q == '2':
        print('\n You climb the ladder and go through the hatch. You appear to be in the living quarters.')
        hatch_q = input('Option 1: You explore the living quarters in hope of finding any information. Option 2: Feeling tired, you decide to take a nap on one of the beds.')
        while True:
            if hatch_q == '1':
                print('\n After looking around, you find a hologram message near one of the beds. The hologram shows a shipmate explaining that an unknown pirate spacecraft has docked onto the ship you are currently in. The hologram cuts out suddenly.')
            elif hatch_q == '2':
                print('\n While sleeping, you are eaten, END OF GAME.')
                break
    else:
        print('\n Invalid response. Try again.')