from collections import deque

N = int(input())
input_list = deque([input() for _ in range(N)])
output_list = deque([])

for i in input_list:
    if 'push' in i:
        _,num = i.split(" ")
        output_list.append(int(num))
    elif 'pop' in i:
        if len(output_list)==0:
            print(-1)
        else:
            print(output_list.pop())
    elif 'size' in i:
        print(len(output_list))
    elif 'empty' in i:
        if len(output_list)==0:
            print(1)
        else:
            print(0)
    elif 'top' in i:
        if len(output_list)==0:
            print(-1)
        else:
            print(output_list[-1])

