from sys import stdin  
from collections import deque

N,M = map(int,stdin.readline().strip().split())
status = (1 << 26) - 1

in_memory = deque()
out_memory = deque()

for _ in range(N):
    word = stdin.readline().strip()
    word_bin = 0
    for w in word:
        w_bin = (1 << ord(w) - 97)
        if word_bin & w_bin != w_bin:
            word_bin+=w_bin

    in_memory.append(word_bin)

pre_cnt = N
ans = []

for _ in range(M):
    o,w = stdin.readline().strip().split()
    tmp_memory = []
    w_bin = (1 << ord(w) - 97)
    if o == '1':
        status-=w_bin
        for _ in range(pre_cnt):
            word_bin = in_memory.popleft()
            if status & word_bin == word_bin:
                in_memory.append(word_bin)
            else:
                out_memory.append(word_bin)

    elif o == '2':
        status+=w_bin
        for _ in range(N-pre_cnt):
            word_bin = out_memory.popleft()
            if status & word_bin == word_bin:
                in_memory.append(word_bin)
            else:
                out_memory.append(word_bin)

    pre_cnt = len(in_memory)
    ans.append(pre_cnt)

print(*ans,sep='\n')
