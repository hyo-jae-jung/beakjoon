from sys import stdin 

N = int(stdin.readline().strip())
rest_apples = 0
for _ in range(N):
    students,apples = map(int,stdin.readline().strip().split())
    rest_apples+=apples%students

print(rest_apples)
