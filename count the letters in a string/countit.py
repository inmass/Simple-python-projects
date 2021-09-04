from string import ascii_lowercase
def countit():
    print('Insert your string:')
    string = input()
    letters = []
    ifthereis = []
    for i in ascii_lowercase:
        letters.append(i)
    for x in letters:
        if string.count(x)>0:
            result = f'{x}:{string.count(x)}'
            ifthereis.append(result)

    print('  '.join(ifthereis))

countit()
