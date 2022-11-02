import sys

N = int(sys.stdin.readline().strip())
words = set((lambda x:(x,len(x)))(sys.stdin.readline().strip()) for _ in range(N))
for i,_ in sorted(words,key=lambda x:(x[1],x[0])):
    print(i)
