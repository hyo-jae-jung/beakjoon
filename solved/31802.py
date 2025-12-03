from sys import stdin   

p = int(stdin.readline().strip())
F = list(map(int,stdin.readline().strip().split()))
a,b = map(int,stdin.readline().strip().split())

d = b - a
b-=1
f_length = len(F)

portion_a,remainder_a = a//f_length,a%f_length
portion_b,remainder_b = b//f_length,b%f_length

ans = 0
if portion_a == portion_b:
    for i in range(remainder_a,remainder_b+1):
        ans+=F[i]
else:
    ans+=sum(F)*(portion_b - portion_a - 1)
    for i in range(remainder_a,f_length):
        ans+=F[i]
    for i in range(0,remainder_b+1):
        ans+=F[i]

print(ans)
