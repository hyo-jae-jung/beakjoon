n = 28
s = []

for _ in range(n):
    s.append(int(input()))

dont_submit = []

for i in range(1,31):
    if i not in s:
        dont_submit.append(i)
    
dont_submit.sort()

iter_d = iter(dont_submit)

print(next(iter_d))
print(next(iter_d))
