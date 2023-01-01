import sys

N,B = sys.stdin.readline().strip().split()
B = int(B)
answer = 0
d1 = dict()
for i in range(0,10):
    d1[str(i)]=i 

d2 = dict()
for i,j in enumerate(range(10,36)):
    d2[chr(65+i)]=j

d1.update(d2)

for i,j in enumerate(reversed(N)):
    answer+=d1[j]*B**i

print(answer)
