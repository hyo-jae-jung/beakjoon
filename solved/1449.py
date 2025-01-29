from sys import stdin   

N,L = map(int,stdin.readline().strip().split())
leaking_pipe = list(map(int,stdin.readline().strip().split()))
leaking_pipe.sort()

ans = 0
remaining_tape = L
for i in leaking_pipe:
    if remaining_tape == L:
        remaining_tape-=1
        loc = i
    else:
        if i - loc <= remaining_tape:
            remaining_tape = remaining_tape - (i - loc)
            loc = i
        else:
            ans+=1
            remaining_tape = L - 1
            loc = i
else:
    if remaining_tape < L:
        ans+=1

print(ans)
