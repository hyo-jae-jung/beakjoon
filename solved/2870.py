from sys import stdin   

N = int(stdin.readline().strip())
nums = []
for _ in range(N):
    t = ''
    for i in stdin.readline().strip():
        if 48 <= ord(i) <= 57:
            t+=i
        else:
            if t:
                nums.append(int(t))
                t = ''
    else:
        if t:
            nums.append(int(t))
            t = ''

for i in sorted(nums):
    print(i)
