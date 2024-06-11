from sys import stdin  

ABC = list(map(int,stdin.readline().strip().split()))
IJK = list(map(int,stdin.readline().strip().split()))

ABCperIJK = [i/j for i,j in zip(ABC,IJK)]
idx = ABCperIJK.index(min(ABCperIJK))
print(*[(round(i - ABC[idx]*j/IJK[idx],6) if ABC[idx]*j%IJK[idx] != 0 else i - ABC[idx]*j//IJK[idx]) for i,j in zip(ABC,IJK)])
