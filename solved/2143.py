from sys import stdin  

T = int(stdin.readline().strip())
n = int(stdin.readline().strip())
A = list(map(int,stdin.readline().strip().split()))
m = int(stdin.readline().strip())
B = list(map(int,stdin.readline().strip().split()))

def perfix_arr(arr):
    result = [0]
    for i in arr:
        result.append(i+result[-1])
    return result

A_perfix = perfix_arr(A)
B_perfix = perfix_arr(B)

def under_T_arr(arr,n):
    result = {}
    for i in range(1,n+1):
        for j in range(i):
            if not result.get(val:=arr[i] - arr[j]):
                result.update({val:0})
            result[val]+=1
        j+=1
    return result

A_under_T = under_T_arr(A_perfix,n)
B_under_T = under_T_arr(B_perfix,m)

ans = 0
for key,value in A_under_T.items():
    if B_under_T.get(T-key):
        ans+=value*B_under_T.get(T-key)

print(ans)
