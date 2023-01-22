from sys import stdin 

N = int(stdin.readline().strip())
one_friend_list = [list(stdin.readline().strip()) for _ in range(N)]

one_friend_dict = dict()

for i in range(N):
    one_friend_dict[i]=[]

for i in range(N):
    for j in range(N):
        if one_friend_list[i][j] == 'Y':
            one_friend_dict[i].append(j)

two_friend_dict = dict()

for i in range(N):
    two_friend_dict[i]=[]

for i in range(N):
    two_friend_dict[i] = len(set(one_friend_dict[i] + sum([one_friend_dict[j] for j in one_friend_dict[i]],[]))-set([i]))

print(max(two_friend_dict.values()))
