from sys import stdin  
from datetime import datetime, timedelta 

N = int(stdin.readline().strip())
ans = datetime(2014,4,1) + timedelta(days=N)
print(''.join([str(ans.year),'-',str(ans.month).zfill(2),'-',str(ans.day).zfill(2)]))
