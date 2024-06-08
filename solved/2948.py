from sys import stdin  
import datetime

D,M = map(int,stdin.readline().strip().split())
num_to_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
print(num_to_week[datetime.date(2009,M,D).weekday()])
