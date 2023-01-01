import sys, math

N,S = map(int,sys.stdin.readline().strip().split())
A = map(int,sys.stdin.readline().strip().split())
diff_list = [abs(S-i) for i in A]

answer = diff_list.pop()
for i in diff_list:
    answer = math.gcd(answer,i)
    if answer == 1:
        break

print(answer)
