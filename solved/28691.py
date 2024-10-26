from sys import stdin

S = stdin.readline().strip()
m = {
    'M':"MatKor",
    'W':"WiCys",
    'C':"CyKor",
    'A':"AlKor",
    '$':"$clear"
}
print(m[S])
