from sys import stdin  

relation = {
'-':0,
'\\':1,
'(':2,
'@':3,
'?':4,
'>':5,
'&':6,
'%':7,
'/':-1,
}

ans = []

while (input_8:=stdin.readline().strip()) != "#":
    output_10 = 0
    for i,j in zip(input_8,range(len(input_8)-1,-1,-1)):
        output_10+=relation[i]*(8**j)
    ans.append(output_10)

print(*ans,sep='\n')
