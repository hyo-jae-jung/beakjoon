from sys import stdin 

a,b,c = map(int,stdin.readline().strip().split())

if a+b == c:print(f"{a}+{b}={c}")
elif a-b == c:print(f"{a}-{b}={c}")
elif a*b == c:print(f"{a}*{b}={c}")
elif a/b == c:print(f"{a}/{b}={c}")
elif b+c == a:print(f"{a}={b}+{c}")
elif b-c == a:print(f"{a}={b}-{c}")
elif b*c == a:print(f"{a}={b}*{c}")
elif b/c == a:print(f"{a}={b}/{c}")
