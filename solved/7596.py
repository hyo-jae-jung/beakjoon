from sys import stdin  

ans = []
while (n:=int(stdin.readline().strip())) != 0:
    play_list = []
    for _ in range(n):
        play_list.append(stdin.readline().strip())
    ans.append(sorted(play_list))

for i in range(len(ans)):
    print(i+1)
    print(*ans[i],sep='\n')

