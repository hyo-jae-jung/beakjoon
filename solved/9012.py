T = int(input())

data_list =[list(input()) for _ in range(T)]
for i in data_list:
    sum=0
    for j in i:
        if j=="(":
            sum+=1
        elif j==")":
            sum-=1
        if sum < 0:
            print("NO")
            break
    else:
        if sum==0:
            print("YES")
        else:
            print("NO")
