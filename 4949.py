import sys

answer = []
loop_cnt=0
while True:
    sentence = sys.stdin.readline().rstrip()
    if sentence =='.': break
    temp=[]
    for i in sentence:
        try:
            if i == '(':
                temp.append(i)
            elif i == '[':
                temp.append(i)
            elif i == ')':
                if temp.pop() != '(':
                    answer.append('no')
                    break
            elif i == ']':
                if temp.pop() != '[':
                    answer.append('no')
                    break
        except:
            answer.append('no')
            break

    if len(answer)!=loop_cnt:
        if len(temp)==0:
            answer.append('yes')
        else:
            answer.append('no')
    loop_cnt+=1

for i in answer:
    print(i)
