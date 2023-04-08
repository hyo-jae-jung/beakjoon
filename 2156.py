import sys
sys.setrecursionlimit(10**5)

n = int(sys.stdin.readline().strip())
wines = []
for _ in range(n):
    wines.append(int(sys.stdin.readline().strip()))

wines_drank = []
memo = [[-1 for _ in range(2+1)] for _ in range(n+1)]

def drink_or_not(position:int=0,condition:int=0,an_amount_of_wine:int=0):    

    if position >= n:
        wines_drank.append(an_amount_of_wine)
        return True

    #pass
    if memo[position][0] < an_amount_of_wine:
        drink_or_not(position=position+1,condition=0,an_amount_of_wine=an_amount_of_wine)

    #drink
    condition+=1
    an_amount_of_wine+=wines[position]
    if condition < 3 and memo[position][condition] < an_amount_of_wine:
        drink_or_not(position=position+1,condition=condition,an_amount_of_wine=an_amount_of_wine)

drink_or_not()
print(max(wines_drank))
