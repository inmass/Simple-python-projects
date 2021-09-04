def numword():
    numbers = {0:'',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',10:'ten',11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen',20:'twenty',30:'thirty',40:'forty',50:'fifty',60:'sixty',70:'seventy',80:'eighty',90:'ninety',100:'one hundred',200:'two hundred',300:'three hundred',400:'four hundred',500:'five hundred',600:'six hundred',700:'seven hundred',800:'eight hundred',900:'nine hundred',1000:'one thousand',1000000:'one million'}
    numberslist = []
    request = input('Enter your number: ')
    request = request.replace(' ','')
    if int(request) in numbers.keys(): #if the number is in the source
        result = numbers[int(request)]
        print(result.capitalize())
    else:
        try:
            for i in request: #takes the input and appending it to the numberslist list
                numberslist.append(i)
            if len(numberslist) == 2: #for tens
                result = f'{numbers[int(numberslist[0])*10]} {numbers[int(numberslist[1])]}.'
            elif len(numberslist) == 3: #for hundreds
                result = f'{numbers[int(numberslist[0])*100]} {numbers[int(numberslist[1])*10]} {numbers[int(numberslist[2])]}.'
            elif len(numberslist) <= 6 and len(numberslist) >= 4: #for thousands
                numberslist1 = numberslist[:-3]
                numberslist2 = numberslist[-3:]
                joined1 = int(''.join(numberslist1))
                joinedteen = int(''.join(numberslist2[1:]))
                if joined1 in numbers and joinedteen in numbers :
                    result = f'{numbers[joined1]} thousand {numbers[int(numberslist2[0])*100]} {numbers[joinedteen]}.'
                else:
                    if len(numberslist1) == 3: #if its like 100 000
                        if joinedteen in numbers:
                            result = f'{numbers[int(numberslist1[0])*100]} {numbers[int(numberslist1[1])*10]} {numbers[int(numberslist1[2])]} thousand {numbers[int(numberslist2[0])*100]} {numbers[joinedteen]}.'
                        else:
                            result = f'{numbers[int(numberslist1[0])*100]} {numbers[int(numberslist1[1])*10]} {numbers[int(numberslist1[2])]} thousand {numbers[int(numberslist2[0])*100]} {numbers[int(numberslist2[1])*10]} {numbers[int(numberslist2[2])]}.'
                    elif len(numberslist1) == 2: #if its like 10 000
                        if joined1 in numbers:
                            result = f'{numbers[joined1]} thousand {numbers[int(numberslist2[0])*100]} {numbers[int(numberslist2[1])*10]} {numbers[int(numberslist2[2])]}.'
                        elif joinedteen in numbers:
                            result = f'{numbers[int(numberslist1[0])*10]} {numbers[int(numberslist1[1])]} thousand {numbers[int(numberslist2[0])*100]} {numbers[joinedteen]}.'
                        else:
                            result = f'{numbers[int(numberslist1[0])*10]} {numbers[int(numberslist1[1])]} thousand {numbers[int(numberslist2[0])*100]} {numbers[int(numberslist2[1])*10]} {numbers[int(numberslist2[2])]}.'
                    else: #if its like 1 000
                        if joinedteen in numbers:
                            result = f'{numbers[int(numberslist1[0])]} thousand {numbers[int(numberslist2[0])*100]} {numbers[joinedteen]}.'
                        else:
                            result = f'{numbers[int(numberslist1[0])]} thousand {numbers[int(numberslist2[0])*100]} {numbers[int(numberslist2[1])*10]} {numbers[int(numberslist2[2])]}.'
            print(result.capitalize())
        except:
            print('The number is too big!')
numword()
