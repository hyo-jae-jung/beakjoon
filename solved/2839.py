N = int(input())

sugar_5kg_count = 0

while sugar_5kg_count*5 <= N:
    sugar_5kg_count += 1

answer = -1

for i in reversed(range(sugar_5kg_count)):
    if (N-i*5)%3 == 0:
        answer = int(i+(N-i*5)/3)
        break

print(answer)
    