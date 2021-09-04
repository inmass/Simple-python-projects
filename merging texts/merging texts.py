import glob2
import datetime
files = glob2.glob('*.txt')
with open(datetime.datetime.now().strftime("%b-%d-%Y--%H-%M-%S")+'.txt','w') as file:
    for i in files:
        with open(i,'r') as e:
            file.write(e.read()+'\n')
