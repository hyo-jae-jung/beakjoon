from sys import stdin 
from datetime import datetime

month,day,year,time = stdin.readline().strip().split()
hour,minute = time.split(':')
months = {
        'January':1, 
        'February':2, 
        'March':3, 
        'April':4, 
        'May':5, 
        'June':6, 
        'July':7, 
        'August':8, 
        'September':9, 
        'October':10, 
        'November':11, 
        'December':12
        }

criteria = (datetime(int(year)+1,1,1,0,0,0) - datetime(int(year),1,1,0,0,0)).days*24*60*60
numerator = datetime(int(year),months[month],int(day[:-1]),int(hour),int(minute),0) - datetime(int(year),1,1,0,0,0)

print(100*(numerator.days*24*60*60 + numerator.seconds)/criteria)
