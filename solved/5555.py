from sys import stdin 

s = stdin.readline().strip()
N = int(stdin.readline().strip())
answer = 0

l = len(s)

for _ in range(N):
    tmp = stdin.readline().strip()
    is_s = tmp[:l]
    tmp = tmp[l:]
    for i in range(l+9):
        if s == is_s:
            answer+=1
            break
        elif tmp:
            t = tmp[0]
            tmp = tmp[1:] + is_s[0]
            is_s = is_s[1:] + t
        else:
            is_s = is_s[1:] + is_s[0]

print(answer)
