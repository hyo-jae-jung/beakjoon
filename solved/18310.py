from sys import stdin 

N = int(stdin.readline().strip())
house_loc = sorted(list(map(int,stdin.readline().strip().split())))
print(house_loc[N//2 - (1 if N%2 == 0 else 0)])
