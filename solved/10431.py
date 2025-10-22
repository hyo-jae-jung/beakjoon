from sys import stdin   

P = int(stdin.readline().strip())
ans = []
for _ in range(P):
    cnt = 0
    l = list(stdin.readline().strip().split())
    stack = []
    for i in l[1:]:
        stack.append(int(i))

        for j in range(len(stack)-1,0,-1):
            if stack[j] < stack[j-1]:
                stack[j],stack[j-1] = stack[j-1],stack[j]
                cnt+=1
            else:
                break

    ans.append((l[0],cnt))

for idx,cnt in ans:
    print(idx,cnt)
