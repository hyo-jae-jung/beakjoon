from sys import stdin 

N,M = [int(i) for i in stdin.readline().strip().split()]

books = []
for _ in range(M):
    stdin.readline()
    books.append([int(i) for i in stdin.readline().strip().split()])

def stack_books(books:list)->str:

    idx = 1
    while any(books):
        for i in range(M):
            if books[i]:
                if books[i][-1] == idx:
                    idx+=1
                    break
        else:
            return 'No'
    else:
        return 'Yes'

if __name__ == "__main__":
    print(stack_books(books))
