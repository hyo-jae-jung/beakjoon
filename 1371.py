from sys import stdin 


words = []
while True:
    word = stdin.readline()
    if word[-1] == '\n':
        words.append(word.strip('\n'))
    else:
        break

print(words)
