from sys import stdin  

K,L = map(int,stdin.readline().strip().split())
h = {}
seq = 1
for _ in range(L):
    s_num = stdin.readline().strip()
    if not h.get(s_num):
        h.update({s_num:0})
    h[s_num] = seq
    seq+=1

for i in sorted(h.items(),key=lambda x:x[1])[:K]:
    print(i[0])
