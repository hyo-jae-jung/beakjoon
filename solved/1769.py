from sys import stdin 

inp = stdin.readline().strip()

i = 0
while len(inp) > 1:
    inp = str(sum(map(int,inp)))
    i+=1

print(i,'YES' if int(inp)%3 == 0 else 'NO',sep='\n')

# i = 0
# while len(inp) > 1:
#     inp = str(eval('+'.join(inp)))
#     i+=1

# print(i,'YES' if int(inp)%3 == 0 else 'NO',sep='\n')
