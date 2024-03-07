from sys import stdin 

N = int(stdin.readline().strip())
s = stdin.readline().strip()

d = {
    'A':{
        'A':'A',
        'G':'C',
        'C':'A',
        'T':'G'
    },
    'G':{
        'A':'C',
        'G':'G',
        'C':'T',
        'T':'A'
    },
    'C':{
        'A':'A',
        'G':'T',
        'C':'C',
        'T':'G'
    },
    'T':{
        'A':'G',
        'G':'A',
        'C':'G',
        'T':'T'
    }
}

first = s[-1]

for i in range(N-2,-1,-1):
    first = d[first][s[i]]

print(first)
