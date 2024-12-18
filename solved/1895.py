from sys import stdin  

R,C = map(int,stdin.readline().strip().split())
I = []
for _ in range(R):
    I.append(list(map(int,stdin.readline().strip().split())))

T = int(stdin.readline().strip())

def median(arr):
    arr.sort()
    l = len(arr)
    if l%2:
        return arr[l//2]
    else:
        return sum(arr[l//2-1,l//2+1])//2
    
ans = 0

for i in range(R-2):
    for j in range(C-2):
        tmp_arr = []
        for k in range(i,i+3):
            for l in range(j,j+3):
                tmp_arr.append(I[k][l])
        if median(tmp_arr) >= T:
            ans+=1

print(ans)
