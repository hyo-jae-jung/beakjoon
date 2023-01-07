from sys import stdin

n = int(stdin.readline().strip())

# def naive_fibonacci(n):
#     if n == 1 or n == 2: 
#         return 1
#     else: 
#         return naive_fibonacci(n-1) + naive_fibonacci(n-2)

def dp_fibonacci(n):
    arr = [None,1,1]
    if n < len(arr):
        return arr[n]

    for i in range(3,n+1):
        arr.append(arr[i-1] + arr[i-2])

    return arr[n]

print(dp_fibonacci(n),n-2)
