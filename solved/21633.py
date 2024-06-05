from sys import stdin  

k = int(stdin.readline().strip())

ans = k*0.01+25
if ans < 100:
    print(f"{100:.2f}")
elif ans > 2000:
    print(f"{2000:.2f}")
else:
    print(f"{k*0.01+25:.2f}")
