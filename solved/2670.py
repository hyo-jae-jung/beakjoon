from sys import stdin 

N = int(stdin.readline().strip())
nums = [float(stdin.readline().strip()) for _ in range(N)]

present_mult = nums[0]
max_mult = nums[0]
for i in nums[1:]:
    present_mult = max(present_mult*i,i)
    max_mult = max(max_mult,present_mult)

print(f"{max_mult:.3f}")

