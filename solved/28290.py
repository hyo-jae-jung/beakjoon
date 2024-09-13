from sys import stdin  

S = stdin.readline().strip()

if S == "fdsajkl;" or S == "jkl;fdsa":
    print("in-out")
elif S == "asdf;lkj" or S == ";lkjasdf":
    print("out-in")
elif S == "asdfjkl;":
    print("stairs")
elif S == ";lkjfdsa":
    print("reverse")
else:
    print("molu")
    