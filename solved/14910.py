from sys import stdin  

arr = list(map(int,stdin.readline().strip().split()))
ans = 'Good'
for i in range(1,len(arr)):
    if arr[i] < arr[i-1]:
        ans = 'Bad'
        break

print(ans)
