from sys import stdin   

t = int(stdin.readline().strip())
ans = []
for _ in range(t):
    _ = stdin.readline().strip()
    n,e = map(int,stdin.readline().strip().split())
    num_ticket = {}
    for i in range(1,n+1):
        num_ticket.update({i:i})

    for new_ticket in range(0,-e,-1):
        num_ticket[int(stdin.readline().strip())] = new_ticket
        
    ans.append(sorted(num_ticket.items(),key=lambda x:x[1])[-1][0])

print(*ans,sep="\n")
