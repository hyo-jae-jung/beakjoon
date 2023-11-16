from sys import stdin 
import re

s = stdin.readline().strip()
happy = re.compile(':-\)')
sad = re.compile(':-\(')
happy_cnt = len(re.findall(happy,s))
sad_cnt = len(re.findall(sad,s))

if happy_cnt == 0 and sad_cnt == 0:
    print('none')
elif happy_cnt - sad_cnt > 0:
    print('happy')
elif happy_cnt - sad_cnt < 0:
    print('sad')
else:
    print('unsure')
    