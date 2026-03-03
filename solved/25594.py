from sys import stdin 
from collections import deque

S = stdin.readline().strip()

d ={
"a":("aespa",len("aespa")),
"b":("baekjoon",len("baekjoon")),
"c":("cau",len("cau")),
"d":("debug",len("debug")),
"e":("edge",len("edge")),
"f":("firefox",len("firefox")),
"g":("golang",len("golang")),
"h":("haegang",len("haegang")),
"i":("iu",len("iu")),
"j":("java",len("java")),
"k":("kotlin",len("kotlin")),
"l":("lol",len("lol")),
"m":("mips",len("mips")),
"n":("null",len("null")),
"o":("os",len("os")),
"p":("python",len("python")),
"q":("query",len("query")),
"r":("roka",len("roka")),
"s":("solvedac",len("solvedac")),
"t":("tod",len("tod")),
"u":("unix",len("unix")),
"v":("virus",len("virus")),
"w":("whale",len("whale")),
"x":("xcode",len("xcode")),
"y":("yahoo",len("yahoo")),
"z":("zebra",len("zebra")),
}

i = 0
val = []
while i < len(S):
    if d[S[i]][0] == S[i:i+d[S[i]][1]]:
        val.append(S[i])
    else:
        print("ERROR!")
        break
    i+=d[S[i]][1]
else:
    print("It's HG!")
    print(''.join(val))
