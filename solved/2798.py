from itertools import combinations

N,M = input().split()
print(max([sum(i) for i in combinations([int(i) for i in input().split()],3) if sum(i) <= int(M)]))


"""
이 문제로 가져가야 할 키워드

부르트 포스
from itertools import combinations


문제를 읽고 combination이 필요하다고 생각
부르트 포스가 뭔지는 문제를 푼 다음 검색해서 암

"""

