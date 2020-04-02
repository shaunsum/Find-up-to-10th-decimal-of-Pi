import math

while True:
    try:
        user_input = int(input('Please enter a number between 0 and 10: '))
    except ValueError:
        print('Sorry, I am looking for a number between 0 and 10.')
        continue
    if user_input > 10:
        print('Sorry, I am looking for a number between 0 and 10')
        continue
    else:
        print('Pi to the {}th decimal is'.format(user_input), math.pi.__round__(int(user_input)))
        break