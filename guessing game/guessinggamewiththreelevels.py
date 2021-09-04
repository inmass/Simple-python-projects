# %%
def threelvls():
    import random
    x1 = random.randint(1,30)
    x2 = random.randint(1,60)
    x3 = random.randint(1,100)
    guesses1 = 0
    guesses2 = 0
    guesses3 = 0
    guess = 0
    maxg1 = 3
    maxg2 = 6
    maxg3 = 9
    choice = 0
    decision = 0
    choice = int(input('Chose your level (1 or 2 or 3): '))
    if choice == 1:
        while guess != x1 and guesses1 < maxg1 :
            guess = int(input('Make your guess: '))
            guesses1 += 1
            if guess < 1 or guess > 30 :
                print('OUT OF BONDS')
            elif guess > x1 :
                print('Too much!')
            elif guess < x1 :
                print('Too less!')
        if guess == x1:
            print(f'You got it! \nIt took you {guesses1} guesses to get it right!')
        else :
            print(f'You are out of guesses! \nThe right guess was: {x1}')

    elif choice == 2:
        while guess != x2 and guesses2 < maxg2 :
            guess = int(input('Make your guess: '))
            guesses2 += 1
            if guess < 1 or guess > 60 :
                print('OUT OF BONDS')
            elif guess > x2 :
                print('Too much!')
            elif guess < x2 :
                print('Too less!')
        if guess == x2:
            print(f'You got it! \nIt took you {guesses2} guesses to get it right!')
        else :
            print(f'You are out of guesses! \nThe right guess was: {x2}')

    elif choice == 3:
        while guess != x3 and guesses3 < maxg3 :
            guess = int(input('Make your guess: '))
            guesses3 += 1
            if guess < 1 or guess > 100 :
                print('OUT OF BONDS')
            elif guess > x3 :
                print('Too much!')
            elif guess < x3 :
                print('Too less!')
        if guess == x3:
            print(f'You got it! \nIt took you {guesses3} guesses to get it right!')
        else :
            print(f'You are out of guesses! \nThe right guess was: {x3}')
    
    decision = input('Do you want to play again ? (yes or no) : ')
    while decision.upper() == 'YES':
        from IPython.display import clear_output
        clear_output()
        threelvls()
        break

# %%
print('Hello! this is a number guessing game with three levels..\n\n-The first one comes with 3 tries to guess the right number between 1 and 30.\n-The second one comes with 6 tries to guess the right number between 1 and 60.\n-And the the third one comes with 9 tries to guess the right number between 1 and 100.')
threelvls()

# %%
'''
##### 
'''