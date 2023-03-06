from sys import stdin 

N = stdin.readline().strip()
F = int(stdin.readline().strip())
cnt = 0
while int(N[:-2]+str(cnt).rjust(2,'0'))%F != 0:    
    cnt+=1

print(str(cnt).rjust(2,'0'))
