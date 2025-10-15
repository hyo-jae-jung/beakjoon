from sys import stdin  

N,X,Y = map(int,stdin.readline().strip().split())
A = list(map(int,stdin.readline().strip().split()))

meal_cnt = 0
rest = 0
diff = Y - X
for a in A:
    p_meal_cnt = a//X
    p_rest = a%X
    rest+=(p_rest - p_meal_cnt*diff if p_rest > p_meal_cnt*diff else 0)
    meal_cnt+=p_meal_cnt

print(meal_cnt)
print(rest)
