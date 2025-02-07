from sys import stdin   

w,h = map(int,stdin.readline().strip().split())
print(w+h-(w**2+h**2)**0.5)
