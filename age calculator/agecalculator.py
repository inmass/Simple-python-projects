import datetime
current = str(datetime.datetime.now())[0:11].replace('-','/')
name = str(input('Name:\n'))
birth = str(input('Birth day (YYYY/MM/DD):\n'))
birthlist = []
agelist = []
ymd = []
todayslist =[int(current[8:10]),int(current[5:7]),int(current[0:4])] #date is listed on list of ints
#making sure that its written right
if not birth.count('/')==2 :
    birth = input('The date you have submitted is wrong, please make sure you wrote it down in the right way AAAA/MM/JJ:\n')
    if not birth.count('/')==2:
        birth = input('LAST CHANCE!, please make sure you wrote it down in the right way AAAA/MM/JJ:\n')
#appending the date to the birthlist
try:
    birthlist.append(int(birth[8:10]))
    birthlist.append(int(birth[5:7]))
    birthlist.append(int(birth[0:4]))
except:
    pass
try:
    #calculating the age
    #this one is for days
    if todayslist[0]<birthlist[0]:
        #we set an if statement if the month is 31 or 30
        birthlist[1] = birthlist[1] + 1
        birthlist[0] = birthlist[0] + 1
        #if the month's days are 32
        if birthlist[1] in [1,3,5,7,8,10,12]:
            agelist.append(todayslist[0]-birthlist[0]+31)
        #if the month's days are 30
        elif birthlist[1] in [4,6,9,11]:
            agelist.append(todayslist[0]-birthlist[0]+30)
        #if the month's days are 28 or 29
        else:
            if birthlist[2]%4 == 0:
                agelist.append(todayslist[0]-birthlist[0]+29)
            else:
                agelist.append(todayslist[0]-birthlist[0]+28)

    else:
        agelist.append(todayslist[0]-birthlist[0])
    #this one is for months
    if todayslist[1]<birthlist[1]:
        agelist.append(todayslist[1]+12-birthlist[1])
        birthlist[2]= birthlist[2] + 1
    else:
        agelist.append(todayslist[1]-birthlist[1])
    #this one is for years
    agelist.append(todayslist[2]-birthlist[2])
    #now appending to the list for YMD code
    ymd.append('Y'*agelist[2])
    ymd.append('M'*agelist[1])
    ymd.append('D'*agelist[0])
    #now we getting ready to give the answers
    print(f'THANK YOU {name.lower().capitalize()}!')
    print('So your age is:')
    print(f'{agelist[2]} years, {agelist[1]} months and {agelist[0]} days .')
    print(''.join(ymd))
except:
    print(f'The birth date was wrong, see you {name.lower().capitalize()}!')
