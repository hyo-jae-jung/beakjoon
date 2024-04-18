from sys import stdin 

left,right = stdin.readline().strip().split("(^0^)")

def ans_cnt(l):
    cnt = 0
    for i in l:
        if i == "@":    
            cnt+=1
    return cnt

print(ans_cnt(left),ans_cnt(right))
