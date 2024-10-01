from sys import stdin  

N = int(stdin.readline().strip())
T = list(map(int,stdin.readline().strip().split()))

total_hours = sum(T) + (len(T) - 1)*8
days = total_hours//24 
print(days, total_hours - days*24)
