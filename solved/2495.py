from sys import stdin 

ans = []
for _ in range(3):
    max_seq = 0
    seq = 1
    num = ''
    for i in stdin.readline().strip():
        if i == num:
            seq+=1
        else:
            max_seq = max(max_seq,seq)
            seq = 1
        num = i
    else:
        max_seq = max(max_seq,seq)
    ans.append(max_seq)

print(*ans,sep='\n')
