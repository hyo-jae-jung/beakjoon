from sys import stdin 

N = int(stdin.readline().strip())
nums = [float(stdin.readline().strip())]
for _ in range(N-1):
    nums.append(nums[-1]*float(stdin.readline().strip()))

print(nums)
