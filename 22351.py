from sys import stdin  

S = stdin.readline().strip()

i,j = 0,1
l = 1
while j+l <= len(S):
    if int(S[i]) + 1 == int(S[j:j+l]):
        i+=1
        j+=1
    