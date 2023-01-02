def star(n:int)->str:
    if n==1:
        return '*'
    else:
        temp = ''
        for i in range(3):
            for i in range(3):
                temp+=star(n-1)
            temp+='\n'
        return temp
        
print(star(2))
