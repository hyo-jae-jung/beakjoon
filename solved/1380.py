from sys import stdin 

answer = []
ss = 1
while n:=int(stdin.readline().strip()):
    students = dict()
    for i in range(1,n+1):
        students.update({i:stdin.readline().strip()})

    check = set()
    for _ in range(2*n-1):
        num, _ = stdin.readline().strip().split()
        num = int(num)
        if num not in check:
            check.add(num)
        else:
            check.discard(num)
    ans = check.pop()
    answer.append((ss,students[ans]))
    ss+=1

for i in answer:
    print(*i)
