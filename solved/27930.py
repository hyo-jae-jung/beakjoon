from sys import stdin 

S = stdin.readline().strip()

k='KOREA'
y='YONSEI'

k_buf,y_buf = '',''

k_i,y_i = 0,0

for i in S:
    if i == k[k_i]:
        k_buf+=i
        k_i+=1
    if i == y[y_i]:
        y_buf+=i
        y_i+=1
    if k_buf == k:
        print(k_buf)
        break
    if y_buf == y:
        print(y_buf)
        break
    