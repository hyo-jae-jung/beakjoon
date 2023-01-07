from sys import stdin 

K,N = map(int,stdin.readline().strip().split())
got_lan = [int(stdin.readline().strip()) for _ in range(K)]
got_lan.sort()

k=1
u = got_lan[0]

while sum([int(i/(u/k)) for i in got_lan]) <= N:
    k+=1

def f(u,k):
    return u/k if k > 1 else 2*u/k

data = range(int(f(u,k)),int(f(u,k-1))+1)
start = 0
end = len(data)-1

answer = 0
while start <= end:
    mid = (start+end)//2
    c = sum([int(i/data[mid]) for i in got_lan])
    if c == N:
        answer = data[mid]
        break
    elif c > N:
        start = mid + 1
    else:
        end = mid - 1

while answer:
    answer+=1
    if sum([int(i/answer) for i in got_lan]) != N:
        break

print(answer-1)
    