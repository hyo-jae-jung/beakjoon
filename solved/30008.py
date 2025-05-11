from sys import stdin  

N,K = map(int,stdin.readline().strip().split())
G = list(map(int,stdin.readline().strip().split()))

def grade(p):
    if p <= 4:return 1
    if p <= 11:return 2
    if p <= 23:return 3
    if p <= 40:return 4
    if p <= 60:return 5
    if p <= 77:return 6
    if p <= 89:return 7
    if p <= 96:return 8
    if p <= 100:return 9

print(*list(map(lambda x:grade((x*100)//N),G)))
