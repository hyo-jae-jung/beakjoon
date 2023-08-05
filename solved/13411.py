from sys import stdin 

N = int(stdin.readline().strip())

arr = []
for i in range(N):
    arr.append(list(map(int,stdin.readline().strip().split())) + [i+1])

arr.sort(key=lambda x:((((x[0]**2+x[1]**2)**0.5))/x[2],x[3]))

for _,_,_,i in arr:
    print(i)
    