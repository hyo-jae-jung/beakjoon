from sys import stdin 

N = int(stdin.readline().strip())
books = []
for _ in range(N):
    books.append(stdin.readline().strip())

d = dict.fromkeys(set(books),0)

for i in books:
    d[i]+=1

s = sorted(d.items())
print(sorted(s,key=lambda x:x[1], reverse=True)[0][0])
