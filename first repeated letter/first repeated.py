from string import ascii_lowercase
from string import ascii_uppercase
from string import punctuation

def firstreplet(textornumberorcar):
    if type(textornumberorcar) == str:
        repeated = []
        letterspuncnum = ['0','1','2','3','4','5','6','7','8','9']
        for i in ascii_lowercase:
            letterspuncnum.append(i)
        for y in ascii_uppercase:
            letterspuncnum.append(y)
        for z in punctuation:
            letterspuncnum.append(z)
        for x in letterspuncnum:
            if textornumberorcar.count(x) > 1:
                repeated.append(x)
    elif type(textornumberorcar) == int:
        listed = []
        numbers = [0,1,2,3,4,5,6,7,8,9]
        repeated = []
        for i in str(textornumberorcar):
            listed.append(int(i))
        for x in numbers:
            if listed.count(x)>1:
                repeated.append(x)
    if len(repeated)>0:
        print(repeated[0])
    else:
        print('No object is repeated.')

firstreplet('''*l1J?)yn%R[}9~1"=k7]9;0[$''')
