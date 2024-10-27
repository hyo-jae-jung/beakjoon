from sys import stdin  

S = stdin.readline().strip()
print('cute' if 'driip' == S[len(S)-5:] else 'not cute')
