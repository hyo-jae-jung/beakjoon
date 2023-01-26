from sys import stdin 

cnt = 0

for i in range(8):    
    row = list(stdin.readline().strip()[i%2::2])
    while row:
        temp = row.pop()
        if temp == 'F':
            cnt+=1

print(cnt)
