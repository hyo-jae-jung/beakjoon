from sys import stdin 
from datetime import date

today = date(*map(int,stdin.readline().strip().split()))
d_day = date(*map(int,stdin.readline().strip().split()))

if (today.year + 1000 < d_day.year) or (today.year + 1000 == d_day.year and (today.month,today.day) <= (d_day.month,d_day.day)):
    print('gg')
else:
    print('D-'+str(d_day.toordinal()-today.toordinal()))
    