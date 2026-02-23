from sys import stdin 

N = int(stdin.readline().strip())
dictionary = []
for _ in range(N):
    val = 0
    for alphabet in stdin.readline().strip():
        val|=(1 << (ord(alphabet) - 97))
    dictionary.append(val)

visited = [True]*N
ans = 0
def solution(cnt=0,val=0,idx=0):
    global N,dictionary,visited,ans

    if val == ((1 << 26) - 1):
        ans+=1

    if cnt == N:
        return
    
    for i in range(idx,N):
        if visited[i]:
            visited[i] = False
            solution(cnt+1,val | dictionary[i],i+1)
            visited[i] = True

solution()
print(ans)
