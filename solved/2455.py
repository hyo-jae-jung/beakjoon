from sys import stdin 

max_people = 0
people = 0
for _ in range(4):
    out,enter = map(int,stdin.readline().strip().split())
    people-=out
    people+=enter
    max_people=max(max_people,people)

print(max_people)
