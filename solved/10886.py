from sys import stdin 

N = int(stdin.readline().strip())
answer = 0
for _ in range(N):
    answer+=1 if int(stdin.readline().strip()) else -1

print("Junhee is" +" not"*(0 if answer > 0 else 1) + " " + "cute!")
