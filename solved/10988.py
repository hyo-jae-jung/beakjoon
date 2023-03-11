import math
word = input()
if word[:math.ceil(len(word)/2)] == ''.join(reversed(word[len(word)//2:])):
    print(1)
else:
    print(0)
