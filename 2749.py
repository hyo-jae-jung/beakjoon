from sys import stdin 

n = int(stdin.readline().strip())

cycle = 15*10**5

def fibonacci(n:int)->int:

    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    arr = [0,1]

    if n < cycle:
        for i in range(2,n+1):
            num = arr[i-1]+arr[i-2]
            arr.append(num)

        return arr[-1]
    else:
        for i in range(2,cycle):
            num = (arr[i-1]+arr[i-2])%100000
            arr.append(num)

        return arr[n%cycle]

print(fibonacci(n)%10**6)
