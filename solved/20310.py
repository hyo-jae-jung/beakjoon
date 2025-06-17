from sys import stdin  

S = stdin.readline().strip()

l = len(S)
one_cnt = sum(map(int,list(S)))
zero_cnt = l - one_cnt
one_cnt = one_cnt//2
zero_cnt = zero_cnt//2

ans = ''
for i in S:
    if i == '0':
        if zero_cnt > 0:
            ans+=i
            zero_cnt-=1
    elif i == '1':
        if one_cnt > 0:
            one_cnt-=1
        else:
            ans+=i

print(ans)
