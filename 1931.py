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
for i in range(len(books1)):
    for j in range(1,len(books1)):
        if books1[i][1] > books1[j][1]:
            break
    else:
        temp.append(books1[i])
        