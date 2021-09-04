import os
#   ASSIGNEMENTS
hours = ['00','01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23']
wakeup = 0
sleep = 0
waketime = 0
sleeptime = 0
wakehours = []
hourtohour = []
tasks = dict()
#FUCTION TO ASK FOR WAKING TIME
def ask_wake():
    global wakeup
    global waketime
    wakeup = input('When do you wake up ? (HH):\n')
    while wakeup not in hours:
        wakeup = input('PLEASE MAKE SURE TO SUBMIT THE HOUR YOU WAKE UP IN TWO NUMBERS (FOR EXAMPLE IF YOU WAKE AT 1pm PLEASE TYPE 13):\n')
        continue
    else:
        waketime = f'{wakeup}:00'
        
#FUNCTION TO ASK FOR SLEEPINT TIME
def ask_sleep():
    global sleep
    global sleeptime
    sleep = input('When do you sleep ?:\n')
    while sleep not in hours:
        sleep = input('PLEASE MAKE SURE TO SUBMIT THE HOUR YOU SLEEPING IN TWO NUMBERS (FOR EXAMPLE 07 OR 11):\n')
        continue
    else:
        sleeptime = f'{sleep}:00'
    
#Fucntion that checks if the time is right (x and y) are ask_wakeup and ask_sleep and its not called alone
def right_check():
    if int(wakeup)==int(sleep):
        falsetime = True
        return falsetime
        
#FUNCTION THAT CREATS WAKEHOURS
def wake_hours_creation():
    global wakehours
    for i in hours:
        if int(wakeup)<int(sleep) :
            wakehours = hours[hours.index(wakeup):hours.index(sleep)+1]
        elif int(wakeup)>int(sleep):
            wakehours = hours[hours.index(wakeup)::] + hours[0:hours.index(sleep)+1]

#FUNCTION THAT CALCULATES THE HOUR TO HOUR
def hour_to_hour():
    global hourtohour
    for i in range(1,int(len(wakehours))):
        hourtohour.append(f'{wakehours[i-1]}:00 to {wakehours[i]}:00')

#FUNCTION THAT ASKS FOR TASKS
def task_ask():
    global tasks
    for i in range(int(len(hourtohour))):
        tasks.update({hourtohour[i]:input(f'Submit your task for {hourtohour[i]}:\n')})
        os.system('cls')

#FUNCTION TO PRINT THE TABLE
def table_print():
    length = max([len(i) for i in tasks.values()])
    for i,j in tasks.items():
        print('-'*(36+length))
        print('∣∣ ' + i + '      ∣∣      ' + j + ' '*(length-int(len(j))) + '   ∣∣')
    print('-'*(36+length))
#RUNNING PROGRAM BY FUNCS
os.system('cls')
ask_wake()
os.system('cls')
ask_sleep()
os.system('cls')
if right_check():
    print('\nSorry but the time you submitted is wrong!')
else:
    wake_hours_creation()
    hour_to_hour()
    task_ask()
    os.system('cls')
    print(f'\nYou literally have {int(len(hourtohour))} hours! Spend it RIGHT!')
    print(f'So here is your time management worksheet with the time from {waketime} to {sleeptime} :)\n')
    table_print()