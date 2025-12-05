from sys import stdin   

c,e,m = map(int,stdin.readline().strip().split())
ans = ["impossible"]
if c == 4 and e%2 == 0:
    half_e = e//2
    if (D:=half_e**2 - 4*m) >= 0:
        import math
        sqrt_d = math.isqrt(D)
        if sqrt_d*sqrt_d == D:
            portion = (half_e + sqrt_d)/2
            if portion%1 == 0:
                ans = [int(portion+2),int(half_e-portion+2)]
                ans.sort(reverse=True)

print(*ans)
