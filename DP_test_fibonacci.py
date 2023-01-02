from time import time

s1 = time()

def fibo_naive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo_naive(n-1) + fibo_naive(n-2)

print(fibo_naive(10), 'O(2**n)')
print(f'{time()-s1:.5f}')

s2 = time()

# naive한 방식은 subproblem을 계속 계산해야 돼서 시간복잡도가 O(2**n)이다.
# subproblem을 array에 저장하는 방식으로 시간복잡도를 줄일 수 있다.

fib_arr = [0,1]

def fibo_recur_dp(n):
    if n < len(fib_arr):
        return fib_arr[n]
    else:
        fib = fibo_recur_dp(n-1) + fibo_recur_dp(n-2)
        fib_arr.append(fib)
        return fib

print(fibo_recur_dp(10), 'O(n)')
print(f'{time()-s2:.5f}')

# top down 방식은 RecursionError에 취약함 이를 bottom up방식으로 바꾸면 해결 가능

def fib_dp(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    fib_array = [0,1]

    for i in range(2,n+1):
        num = fib_array[i-1] + fib_array[i-2]
        fib_array.append(num)
    return fib_array[n]

print(fib_dp(10000))
# bottom up 방식으로 변경 후 RecursionError 해결

# fib_dp는 subproblem값을 모두 저장했는데 계산에는 마지막 두 값만 있으면 됨
# 마지막 두 값을 제외하고 삭제하면 메모리 효율도 늘릴 수 있음
# by 코드없는 프로그래밍

