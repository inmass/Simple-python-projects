import os
case = [' ']*10
player1 = True
player2 = False
gameon = True
counter = 0

def table():

    os.system('cls')
    print(" ___________ " + "     ___________ ")
    print(f"| {case[1]} | {case[2]} | {case[3]} |" + "    | 1 | 2 | 3 |")
    print("|___|___|___|" + "    |___|___|___|")
    print(f"| {case[4]} | {case[5]} | {case[6]} |" + "    | 4 | 5 | 6 |")
    print("|___|___|___|" + "    |___|___|___|")
    print(f"| {case[7]} | {case[8]} | {case[9]} |" + "    | 7 | 8 | 9 |")
    print("|___|___|___|" + "    |___|___|___|")

def checkver(sp) :
    if case[1] == sp and case[2] == sp and case[3] == sp or case[4] == sp and case[5] == sp and case[6] == sp or case[7] == sp and case[8] == sp and case[9] == sp  :
        return True
    else :
        return False

def checkhor(sp):
    if case[1] == sp and case[4] == sp and case[7] == sp or case[2] == sp and case[5] == sp and case[8] == sp or case[3] == sp and case[6] == sp and case[9] == sp  :
        return True
    else :
        return False

def checkx(sp) :
    if case[1] == sp and case[5] == sp and case[9] == sp or case[3] == sp and case[5] == sp and case[7] == sp :
        return True
    else :
        return False



############GAMEPLAY###########
while gameon:
    table()
    if player1:
        position = int(input('Player 1 chose your position:  '))
        if position < 0 or position > 9:
            print('Please chose between 1 and 9:  ')
        else:
            if case[position] == 'X' or case[position] == 'O':
                print('This position is already taken!:  ')
            else:
                case[position] = 'X'
                player1 = False
                player2 = True
                counter += 1
    elif player2:
        position = int(input('Player 2 chose your position:  '))
        if position < 0 or position > 9:
            print('Please chose between 1 and 9:  ')
        else:
            if case[position] == 'X' or case[position] == 'O':
                print('This position is already taken!:  ')
            else:
                case[position] = 'O'
                player1 = True
                player2 = False
                counter += 1
    if counter >= 9:
        print("It's a draw!")
        gameon = False
    elif checkver('X') or checkhor('X') or checkx('X'):
        gameon = False
        table()
        print('Player1 has won!')
    elif checkver('O') or checkhor('O') or checkx('O'):
        gameon = False
        table()
        print('Player2 has won!')

# %%


# %%
