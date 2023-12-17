from sys import stdin 

A,B = map(int,stdin.readline().strip().split())
N = int(stdin.readline().strip())
memorize_frequencies = [abs(A-B)]
for _ in range(N):
    memorize_frequencies.append(abs(int(stdin.readline().strip())-B)+1)

print(min(memorize_frequencies))
