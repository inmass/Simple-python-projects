def sumofraised():
    resultlist = []
    try:
        base = input('Base: ')
        power = input('Power: ')
        digit = int(base)**int(power)
    except ValueError:
        base = input('Base (Please insert a number): ')
        power = input('Power (Please insert a number): ')
        digit = int(base)**int(power)
    for i in list(str(digit)):
        resultlist.append(int(i))
    print(f'The result of {int(base)}^{int(power)} is: {digit}')
    print(f'The sum of digits of the result is: {sum(resultlist)}')

sumofraised()
