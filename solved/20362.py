from sys import stdin 

N,S = stdin.readline().strip().split()

chat = []
ans = ''
loc = 0
cnt = 0
for i in range(int(N)):
    user, is_ans = stdin.readline().strip().split()
    if user == S:
        ans = is_ans
        loc = i
    chat.append((user,is_ans))
for i in range(loc):
    if chat[i][1] == ans:
        cnt+=1

print(cnt)
