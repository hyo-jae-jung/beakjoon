from sys import stdin 

G = int(stdin.readline().strip())

i,j=1,2
answer = []
while i <= j and j <= 1e5:
    g = j**2 - i**2
    if G > g:
        j+=1
    elif G < g:
        i+=1
    else:
        answer.append(j)
        j+=1

print(*answer,sep='\n') if answer else print(-1)

