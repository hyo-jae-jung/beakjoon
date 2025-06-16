from sys import stdin  

R,G,B = map(int,stdin.readline().strip().split())
print(sum(map(lambda x:x//3,[R,G,B])) + min(max(t:=list(map(lambda x:x%3,[R,G,B]))),sum(map(lambda x:1 if x>0 else 0,t))))
