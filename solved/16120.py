from sys import stdin  

S = stdin.readline().strip()
stack = []

for s in S:
    if stack.__len__() <= 1 and s == 'A':
        print('NP')
        break
    
    if stack.__len__() < 3:
        stack.append(s)
        continue

    if stack.__len__() > 2 and stack[-1] == 'A' and s == 'A':
        print('NP')
        break

    if stack[-3]+stack[-2]+stack[-1]+s == 'PPAP':
        for _ in range(2):
            stack.pop()
    else:
        stack.append(s)

else:
    if "".join(stack) == 'P':
        print("PPAP")
    else:
        print("NP")
