from sys import stdin  

T = int(stdin.readline().strip())

def check_round(n):
    if n<=25:
        return "World Finals"
    if n<=1000:
        return "Round 3"
    if n<=4500:
        return "Round 2" 
    return "Round 1"

ans = []
for i in range(T):
    ans.append(f"Case #{i+1}: " + check_round(int(stdin.readline().strip())))

print(*ans ,sep='\n')
