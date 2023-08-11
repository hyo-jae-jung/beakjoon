from sys import stdin 

N = stdin.readline().strip()

left = 0
right = len(N)-1
if left == right:
    answer = 'NO'
else:
    left_val,right_val = int(N[left]),int(N[right])
    while left < right-1:
        if left_val == 0 and right_val > 0:
            right-=1
            right_val*=int(N[right])
        elif right_val == 0 and left_val > 0:
            left+=1
            left_val*=int(N[left])
        elif left_val == 0 and right_val == 0:
            break
        else:
            if left_val > right_val:
                right-=1
                right_val*=int(N[right])
            else:
                left+=1
                left_val*=int(N[left])
    
    answer = 'YES' if left_val == right_val else 'NO'

print(answer)
