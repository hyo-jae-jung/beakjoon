from sys import stdin 

L,R = [i for i in stdin.readline().strip().split()]

answer = 0

if len(L) == len(R):
    i=0
    while i < len(L)-1:
        if all([L[i] == '8', R[i] == '8']):
            answer+=1
        elif L[i] != R[i]:
            break
        i+=1
    else:
        if all([L[-1] == '8', R[-1] == '8']):
            answer+=1
    
print(answer)
