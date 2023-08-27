from sys import stdin 

N,M = map(int,stdin.readline().strip().split())
J = int(stdin.readline().strip())
basket = [1,M]
diff = 0
for _ in range(J):
    tmp = int(stdin.readline().strip())
    gap = 0
    if basket[0] > tmp:
        gap = basket[0] - tmp
        basket = [i - gap for i in basket]
    elif basket[1] < tmp:
        gap = tmp - basket[1]
        basket = [i + gap for i in basket]
    diff+=gap

print(diff)
