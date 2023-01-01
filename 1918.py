import sys

input = list(sys.stdin.readline().strip())

def solution(input:list,mark:str) -> list:
    loc = input.index(mark)
    if mark == ')':
        a = loc-4
        b = loc-3
        c = loc-1
        d = loc-2
        e = loc+1
    else:
        a = loc-1
        b = loc-1
        c = loc+1
        d = loc
        e = loc+2
    return input[:a] + [''.join([input[b],input[c],input[d]])] + input[e:]

while ')' in input:
    input = solution(input,')')

i=0
while any(['*' in input, '/' in input]):
    if input[i] in ['*','/']:
        input = solution(input,input[i])
        i=0
    else:
        i+=1

i=0
while any(['+' in input, '-' in input]):
    if input[i] in ['+','-']:
        input = solution(input,input[i])
        i=0
    else:
        i+=1

print(*input)
