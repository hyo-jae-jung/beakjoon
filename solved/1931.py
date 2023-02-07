from sys import stdin 
from collections import deque 

N = int(stdin.readline().strip())
books = []
for _ in range(N):
    books.append(list(map(int,stdin.readline().strip().split())))
    
books = deque(sorted(books,key=lambda x:(x[0],x[1])))
answer = []
answer.append(books.popleft())

while books:
    #change
    if answer[-1][1] > books[0][1]:
        answer.pop()
        answer.append(books.popleft())
    #insert
    elif answer[-1][1] <= books[0][0]:
        answer.append(books.popleft())
    #remove
    else:
        books.popleft()

print(len(answer))
