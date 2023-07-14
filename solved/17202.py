from sys import stdin 

A = stdin.readline().strip()
B = stdin.readline().strip()

AB = ''
for i,j in zip(A,B):
    AB+=i+j

while len(AB) > 2:
    temp = ''
    for i in range(1,len(AB)):
        temp+=str(int(AB[i])+int(AB[i-1]))[-1]
    AB = temp

print(AB)
