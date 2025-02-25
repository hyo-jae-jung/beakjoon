from sys import stdin   

M,N = map(int,stdin.readline().strip().split())
idx = {
    '1':'one',
    '2':'two',
    '3':'three',
    '4':'four',
    '5':'five',
    '6':'six',
    '7':'seven',
    '8':'eight',
    '9':'nine',
    '0':'zero'
}

numbers = []
for i in range(M,N+1):
    numbers.append((i,' '.join(idx[j] for j in str(i))))

for i,j in enumerate(sorted(numbers,key=lambda x:x[1])):
    if i > 1 and i%10 == 0:
        print()
    print(j[0],end=' ')
