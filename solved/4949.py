import sys

answer = []
while True:
    sentence = sys.stdin.readline().rstrip()
    if sentence =='.': break
    temp=[]
    for i in sentence:
        yn = ''
        try:
            if i == '(':
                temp.append(i)
            elif i == '[':
                temp.append(i)
            elif i == ')':
                if temp.pop() != '(':
                    yn = 'no'
                    break
            elif i == ']':
                if temp.pop() != '[':
                    yn = 'no'
                    break
        except:
            yn = 'no'
            break
    if yn != 'no':
        if len(temp)==0:
            yn = 'yes'
        else:
            yn = 'no'
    
    answer.append(yn)

for i in answer:
    print(i)
