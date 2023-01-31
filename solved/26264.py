from sys import stdin 
import re

N = int(stdin.readline().strip())
words = stdin.readline().strip()

b = re.compile('bigdata')
c = re.compile('security')

b_len = len(b.findall(words))
c_len = len(c.findall(words))

if b_len == c_len:
    print("bigdata? security!")
elif b_len > c_len:
    print("bigdata?")
else:
    print("security!")
