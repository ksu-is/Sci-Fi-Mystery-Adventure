#remember to save and test your code often
print("\n THAD'S SCI-FI MYSTERY GAME!")
print('\n Once you start playing, you will be asked questions throughout the game. You will have two options for each question, and you must enter "1" or "2" to select your answer.')
print('\n Typing "1" will select the first option, and typing "2" will select the second option.')

print('\n .........')
print()

print('You awake in an unfamiliar place. After glancing around, you determine that you are most likely in the cargo deck of a spaceship.')
first_q = input('Option 1: Leave the cargo deck through the main door. Option 2: Leave the cargo deck by climbing the ladder to the hatch. ')
while True:
    if first_q == '1':
        print('You open the main door and enter a dimly lit hallway. The ground is wet.')
    elif first_q == '2':
        print('You climb the ladder and go through the hatch. You appear to be in the living quarters.')
    else:
        print('Invalid response. Try again.')