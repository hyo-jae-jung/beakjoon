import sys

N = int(input())
M = [int(sys.stdin.readline().strip()) for _ in range(N)]
for i in sorted(M):
    print(i)

"""
sys.stdin.readline()
이거 쓰라는 문제

왜 input보다 sys.stdin.readline()이 빠르냐?
input은 prompt message를 받을 수 있어서. prompt message에 대한 액션이 필요해서 느림
개행문자는 sys.stdin도 삭제해야함
결국 prompt message 차이 같음


https://buyandpray.tistory.com/7
"""