import sys 

N = int(sys.stdin.readline().strip())

a = list(map(int,sys.stdin.readline().strip().split()))
diff_a = []
tmp = 0
for i in range(1,N):
    diff = a[i]-a[i-1]
    if tmp*diff >= 0:
        tmp+=diff
    else:
        diff_a.append(tmp)
        tmp = diff
else:
    diff_a.append(tmp)

max_profit_set = set([0])
tmp = 0

for i in diff_a:
    if i >= 0:
        tmp+=i
        max_profit_set.add(tmp)
    else:
        if tmp+i >= 0:
            tmp+=i
        else:
            tmp = 0

print(max(max_profit_set))
