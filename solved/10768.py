from sys import stdin 
from datetime import datetime 

diff_days = (datetime(2015,int(stdin.readline().strip()),int(stdin.readline().strip())) - datetime(2015,2,18)).days

if diff_days < 0:
    print("Before")
elif diff_days > 0:
    print("After")
else:
    print("Special")
