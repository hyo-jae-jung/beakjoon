from sys import stdin 

A = stdin.readline().strip()
if A[-1] == '4':
    for i in range(1,4):
        print(A[:-1]+str(i))
else:
    s = set()
    A_arr = list(A)
    ans = []

    while 1 < len(A_arr) and len(s) < 3:
        val = A_arr.pop()
        if val not in s:
            s.add(val)
            ans.append(''.join(A_arr)+'4')
    
    print(*ans,sep='\n')
