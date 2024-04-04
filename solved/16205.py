from sys import stdin 

n,s = stdin.readline().strip().split()

def camel_to_list(s):
    l = []
    word = ''
    for i in s:
        if i.islower():
            word+=i
        else:
            if word:
                l.append(word)
            word = i.lower()
    else:
        if word:
            l.append(word)
    return l

def snake_to_list(s):
    return s.split('_')

def pascal_to_list(s):
    return camel_to_list(s)

def list_to_camel(l):
    s = l[0]
    for i in range(1,len(l)):
        s+=l[i].capitalize()
    return s

def list_to_snake(l):
    return '_'.join(l)

def list_to_pascal(l):
    s = ''
    for i in l:
        s+=i.capitalize()
    return s

if n == '1':
    l = camel_to_list(s)
elif n == '2':
    l = snake_to_list(s)
elif n == '3':
    l = pascal_to_list(s)

print(list_to_camel(l))
print(list_to_snake(l))
print(list_to_pascal(l))


