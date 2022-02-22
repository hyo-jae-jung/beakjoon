from collections import deque
K = int(input())
num_list = deque([])
for i in range(K):
    a = int(input())
    if a==0:
        num_list.pop()
    else:
        num_list.append(a)
print(sum(num_list))