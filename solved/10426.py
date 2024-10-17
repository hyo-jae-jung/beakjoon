from sys import stdin  
import datetime

date,days = stdin.readline().strip().split()

year,month,day = map(int,date.split('-'))
print((datetime.datetime(year,month,day) + datetime.timedelta(int(days)-1)).date())
