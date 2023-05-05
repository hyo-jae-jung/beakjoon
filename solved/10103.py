from sys import stdin 

n = int(stdin.readline().strip())

changyoung = 100
sangduk = 100

for _ in range(n):
    c,s = map(int,stdin.readline().strip().split())
    if c > s:
        sangduk-=c
    elif c < s:
        changyoung-=s

print(changyoung,sangduk,sep='\n')
