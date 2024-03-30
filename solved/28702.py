from sys import stdin 

A = stdin.readline().strip()
B = stdin.readline().strip()
C = stdin.readline().strip()
ans = 0
def check(n) -> bool:
    try:
        int(n)
        return True
    except:
        return False
    
if check(A):
    ans = int(A) + 3
elif check(B):
    ans = int(B) + 2
elif check(C):
    ans = int(C) + 1

if ans%3 == 0 and ans%5 == 0:
    print("FizzBuzz")
elif ans%3 == 0 and ans%5 != 0:
    print("Fizz")
elif ans%3 != 0 and ans%5 == 0:
    print("Buzz")
else:
    print(ans)
