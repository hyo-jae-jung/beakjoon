from sys import stdin   

_ = int(stdin.readline().strip())
A = map(int,stdin.readline().strip().split())

print(2**(len(bin(sum(A))[2:])-1))

# from heapq import heapify,heappop,heappush
# heapify(A)
# N = len(A)
# ans = 0
# while N > 1:
#     a = heappop(A)
#     b = heappop(A)

#     if a == b:
#         heappush(A,a+b)
#     else:
#         heappush(A,b)
#     N-=1

# print(*A)
