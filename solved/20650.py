from sys import stdin 

line = list(map(int,stdin.readline().strip().split()))
line_sorted = sorted(line)
print(*(line_sorted[:2]+[line_sorted[-1]-sum(line_sorted[:2])]))
