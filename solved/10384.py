from sys import stdin  

T = int(stdin.readline().strip())
ans = []
for i in range(1,T+1):
    s = stdin.readline().strip()
    arr = [0]*26
    for j in s:
        t = ord(j)
        if 65 <= t <= 90:
            arr[t - 65]+=1
        elif 97 <= t <= 122:
            arr[t - 97]+=1
    
    cnt = min(arr)
    if cnt == 0:
        ans.append(f"Case {i}: Not a pangram")
    elif cnt == 1:
        ans.append(f"Case {i}: Pangram!")
    elif cnt == 2:
        ans.append(f"Case {i}: Double pangram!!")
    else:
        ans.append(f"Case {i}: Triple pangram!!!")

print(*ans,sep='\n')
