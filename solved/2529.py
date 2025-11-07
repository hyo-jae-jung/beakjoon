from sys import stdin   

k = int(stdin.readline().strip())
S = stdin.readline().strip().split()
arr = []
visited = [False]*10

def solution(cnt=0,val=''):
    global k,S,arr,visited
    if cnt == k+1:
        arr.append(val)
        return 
    
    for i in range(10):
        if not visited[i]:
            visited[i] = True
            if cnt == 0:
                solution(cnt+1,val+str(i))
            else:
                if eval(val[-1]+S[cnt-1]+str(i)):
                    solution(cnt+1,val+str(i))
            visited[i] = False

solution()
arr.sort(key=lambda x:(int(x)))
print(arr[-1])
print(arr[0])
