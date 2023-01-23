from sys import stdin 

N = int(stdin.readline().strip())
students = []
for _ in range(N):
    students.append(stdin.readline().strip())
n=1
while N > len(set([i[-1*n:] for i in students])):
    n+=1
else:
    print(n)
    