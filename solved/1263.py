from sys import stdin 

N = int(stdin.readline().strip())
works = []
for _ in range(N):
    works.append(tuple(map(int,stdin.readline().strip().split())))

works.sort(key=lambda x:x[1])

required_time, deadline = works.pop()
time_remaining = deadline - required_time

while works:
    required_time, deadline = works.pop()
    if time_remaining < deadline:
        time_remaining = time_remaining - required_time
    else:
        time_remaining = deadline - required_time

    if time_remaining < 0:
        print(-1)
        break
    
else:
    print(time_remaining)
    