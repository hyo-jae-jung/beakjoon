from sys import stdin   

n,s = map(int,stdin.readline().strip().split())
for _ in range(n):
    lower_skill_bound,upper_skill_bound = map(int,stdin.readline().strip().split())
    if lower_skill_bound <= s <= upper_skill_bound:
        s+=1

print(s)
