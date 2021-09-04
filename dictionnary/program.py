import json
from difflib import get_close_matches
#assignements
on = True
data = json.load(open('data.json','r'))
#function of translation
def define():
    #if the word is in the data file
    if word in data:
        return data[word]
    #if the word exists but with upper first letter
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    #if the word is close to some other word in the data file
    elif len(get_close_matches(word, data.keys())) > 0:
        close = input(f'Did you meant {get_close_matches(word, data.keys())[0]}? (Yes or No): ')
        while close[0].lower() != 'y' and close[0].lower() != 'n':
            close = input('Please answer with Yes or No: ')
            continue
        else:
            if close[0].lower() == 'y':
                return data[get_close_matches(word, data.keys())[0]]
            else:
                return "The word doesn't exist!"

    #if the word doesn't exist
    else:
        return "The word doesn't exist!"
#program works
print('''
Welcome to your dictionnary!
You can start by inserting a word you would like to define.

''')
while on:
    word = input('Enter word: ').lower()
    answer = define()
    #to print a real sentence instead of a string to the user
    if type(answer) == list:
        for item in answer:
            print(item)
    else:
        print(answer)
    #define again
    replay = str(input('Do you want to define another word? (Yes or No): '))
    while replay[0].lower() != 'y' and replay[0].lower() != 'n':
        replay = input('Please enter either Yes or No: ')
        continue
    else:
        if replay[0].lower() == 'y':
            on = True
            continue
        elif replay[0].lower() == 'n':
            on = False
            print('Okay! Good bye.')
    break
