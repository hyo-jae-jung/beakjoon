from sys import stdin 

H,Y = map(int,stdin.readline().strip().split())

ans = []

def solution(h,y):
    if y == 0:
        ans.append(h)
        return True
    
    if y < 0:
        return False
    
    solution(int(h*1.35),y-5)
    solution(int(h*1.2),y-3)
    solution(int(h*1.05),y-1)

solution(H,Y)
print(max(ans))
