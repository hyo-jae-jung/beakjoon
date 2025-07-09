from sys import stdin  

N = int(stdin.readline().strip())
arr = [list(map(int,stdin.readline().strip().split())) for _ in range(N)]
parity_byte = list(map(int,stdin.readline().strip().split()))

odd,even = [],[]
for i in range(1,N+1):
    if sum(arr[i-1])%2 == 0:
        even.append(i)
    else:
        odd.append(i)

if len(even) > len(odd):
    ans1 = 0
    ans2 = f"Byte {odd[0]} is broken"
else:
    ans1 = 1
    ans2 = f"Byte {even[0]} is broken"

for i in range(1,9):
    check = 0
    for j in range(N):
        check+=arr[j][i-1]
    if (check+parity_byte[i-1])%2 != ans1:
        ans3 = f"Bit {i} is broken"
        break

print("Odd" if ans1 == 1 else "Even")
print(ans2)
print(ans3)
