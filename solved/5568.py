from sys import stdin   

n = int(stdin.readline().strip())
k = int(stdin.readline().strip())
cards = [stdin.readline().strip() for _ in range(n)]

s = set()
visited = [False]*n
ans = 0

def solution(card_cnt=0,val=''):

    global n,k,cards,ans,s
    if card_cnt == k:
        if val not in s:
            ans+=1
            s.add(val)
        return
    
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            solution(card_cnt+1,val+cards[i])
            visited[i] = False

solution()
print(ans)
