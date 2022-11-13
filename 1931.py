import sys

N = int(sys.stdin.readline().strip())
books = [tuple(map(int,sys.stdin.readline().strip().split())) for _ in range(N)]
books1 = []
books2 = []
cnt = 0
books.sort()

books1.append(books[0])

for i in range(1,len(books)):
    if books[i][0] != books[i][1] and books[i-1][0] != books[i][0]:
        books1.append(books[i])
    elif books[i][0] == books[i][1]:
        cnt+=1

temp = []
for i in books1:
    temp.append(i)
    for j in books1:
        if temp[-1][1] > j[1]:
            temp.pop()
            temp.append(j)
            break

print(books1)
print(temp)
