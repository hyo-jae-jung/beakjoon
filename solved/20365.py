from sys import stdin 

N = int(stdin.readline().strip())
sentence = stdin.readline().strip()
print(len([i for i in sentence.split(sentence[0]) if i])+1)
