name = input('Type your name: ')
print(f'Welcome {name} to this adventure!')

while True:
    answer = input(f'You are on a road and it\'s come to an end. You can go right or left. Which way would you like to go? ').lower()
    if answer == 'right':
        answer = input(f'You come to a river. You can walk around or swim across? ').lower()
    
        if answer == 'walk around':
            pass
        elif answer == 'swim across':
            print(f'You got eaten by an alligator. You\'re dead.')
            quit()
        else:
            print(f'Not a valid option. Please select walk around or swim across. ')
            continue
        
    elif answer == 'left':
        answer = input(f'You come to a cliff. You can climb down it to save time or you can walk around, which takes longer. Which one?').lower()
         
        if answer == 'Climb down':
            answer = input(f'You got snatched up by an eagle. Do you punch the eagle so he\'ll drop you or do you ride this out?').lower()
            if answer == 'Punch eagle':
                pass
            elif answer == 'Ride this out':
                pass
        elif answer == 'Walk around':
            pass
        else:
            print(f'Not a valid option. Please select walk around or climb down. ')
            continue
    
    else:
        print(f'Not a valid option. Please select right or left.')
        continue
    

    #CONTINUE TO BUILD

