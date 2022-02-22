N = int(input())

def division_sum(x:int)->int:
    return x + sum(map(int,list(str(x))))

for i in range(1,N+1):
    if N == division_sum(i):
        print(i)
        break
else:
    print(0)

    """여기서 배운건 for else의 활용
    """