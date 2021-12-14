T = int(input())
data = []
for i in range(T):
    temp = []
    k = int(input())
    n = int(input())
    temp.append(k)
    temp.append(n)
    data.append(temp)

    how_many_people_in_this_house = []

for g in data:

    k = g[0]
    n = g[1]

    apt = [list(range(1,n+1))]

    for h in range(k):
        ho = []
        for i in range(n):
            ho.append(sum(apt[h][0:1+i]))
        apt.append(ho)

    how_many_people_in_this_house.append(apt[k][n-1])

for i in how_many_people_in_this_house:
    print(i)
