from collections import deque
import sys

N = int(sys.stdin.readline().strip())
queue = deque([])
print_list = []
for _ in range(N):
    input = sys.stdin.readline().strip().split()
    if input[0] == 'push':
        queue.append(input[-1])
    elif input[0] == 'pop':
        if len(queue) != 0:
            print_list.append(queue.popleft())
        else:
            print_list.append(-1)
    elif input[0] == 'size':
        print_list.append(len(queue))
    elif input[0] == 'empty':
        if len(queue) == 0:
            print_list.append(1)
        else:
            print_list.append(0);
    elif input[0] == 'front':
        if len(queue) != 0:
            print_list.append(queue[0])
        else:
            print_list.append(-1)
    elif input[0] == 'back':
        if len(queue) != 0:
            print_list.append(queue[-1])
        else:
            print_list.append(-1)

for i in print_list:
    print(i)
    