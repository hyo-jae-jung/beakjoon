import sys

visited = bytearray(1 << 22)

num = ''
while True:
    i = sys.stdin.read(1)

    if i.isnumeric():
        num+=i
    else:
        num = int(num)
        v,r = num//8,num%8
        br = 1 << r
        if visited[v] & br != br:
            print(num,end=' ')
            visited[v]+=br
        num = ''

    if i == '\n':
        break
