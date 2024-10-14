from sys import stdin  

P = int(stdin.readline().strip())
ans = []
for _ in range(P):
    t = stdin.readline().strip()
    arr = [0]*8
    for i in range(3,41):
        if t[i-3:i] == 'TTT':
            arr[0]+=1
        elif t[i-3:i] == 'TTH':
            arr[1]+=1
        elif t[i-3:i] == 'THT':
            arr[2]+=1
        elif t[i-3:i] == 'THH':
            arr[3]+=1
        elif t[i-3:i] == 'HTT':
            arr[4]+=1
        elif t[i-3:i] == 'HTH':
            arr[5]+=1
        elif t[i-3:i] == 'HHT':
            arr[6]+=1
        elif t[i-3:i] == 'HHH':
            arr[7]+=1

    ans.append(arr)

for i in ans:
    print(*i)
