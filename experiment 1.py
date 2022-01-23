
import csv
import datetime
import os

currentdate = 0
def new(now):
    
    path = f'C:/Users/0526p/.spyder-py3/basics/{now}.csv'
    #p = f'{path}/{now}.csv' 
    with open(path, 'w', newline='') as f:
        thewriter = csv.writer(f)
        thewriter.writerow(['prince 1', 'rajat 2', 'dhruv 2'])

y, m, d = 2001, 3, 12
global now

while d!= 21:
    if currentdate == 0 :
        
        now = datetime.date(y, m, d)
        new(now)
        print(now)
        currentdate = now
        d = d+1
        
    elif currentdate!= now or currentdate == now:
        new(now)
        now = datetime.date(y, m, d)

        print(now)
        d = d+1
        
        
path2='C:/Users/0526p/.spyder-py3/basics'
mylist= os.listdir(path2)
print(mylist)
now3 = datetime.date.today()
path1 = f'{now3}.csv'
if path1 in mylist:
    print('file exits')
    
t = 'prince\nkumar'
print(t)
    

print('Attendance:',
      '\n\tOptions',
      '\tBerif',
      '\n\t1\t\t\tMake new section',
      '\n\t2\t\t\tMark Attendance')
        
        