import sys

N,M = map(int,sys.stdin.readline().strip().split())

never_heard = set(sys.stdin.readline().strip() for _ in range(N))
never_seen = set(sys.stdin.readline().strip() for _ in range(M))

intersection = never_heard & never_seen

print(len(intersection))
for i in sorted(list(intersection)):
    print(i)
