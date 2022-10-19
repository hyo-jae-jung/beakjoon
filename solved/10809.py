S = input()
alphabet = 'abcdefghijklmnopqrstuvwxyz'

answer = ""

for i in alphabet:
    try:
        answer += str(S.index(i)) + " "
    except ValueError:
        answer += str(-1) + " "

print(answer.strip())