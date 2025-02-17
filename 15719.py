from sys import stdin 

N = int(stdin.readline().strip())
arr = stdin.readline().strip()
s = set()
i = 0
while True:
    if arr[i] in s:
        print(arr[i])
        break
    else:
        s.add(arr[i])
        i+=2
    
