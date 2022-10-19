sentence = input().strip().split(" ")
try:
    sentence.remove("")
    print(len(sentence))
except:
    print(len(sentence))
