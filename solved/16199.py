from sys import stdin 
from datetime import datetime

by,bm,bd = map(int,stdin.readline().strip().split())
dy,dm,dd = map(int,stdin.readline().strip().split())

s = (datetime(dy,dm,dd) - datetime(dy,bm,bd)).days

print(dy-by - (1 if s < 0 else 0),dy-by+1,dy-by,sep='\n')
