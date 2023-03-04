from sys import stdin 

answer = []

while True:
    try:
        A,B,C = list(map(int,stdin.readline().strip().split()))
        answer.append(max(B-A-1,C-B-1))
    except:
        break

print(*answer,sep='\n')
