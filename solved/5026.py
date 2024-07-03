from sys import stdin  

N = int(stdin.readline().strip())
ans = []
for _ in range(N):
    if (tmp:=stdin.readline().strip()) != "P=NP":
        ans.append(sum(map(int,tmp.split('+'))))
    else:
        ans.append("skipped")

print(*ans,sep='\n')
