from sys import stdin  

N = int(stdin.readline().strip())
ans = []

arr = {
"a":350.34,
"b":230.90,
"c":190.55,
"d":125.30,
"e":180.90,
}

for _ in range(N):
    A,B,C,D,E = map(int,stdin.readline().strip().split())
    ans.append(arr["a"]*A+arr["b"]*B+arr["c"]*C+arr["d"]*D+arr["e"]*E)

for i in ans:
    print(f"${i:.2f}")
