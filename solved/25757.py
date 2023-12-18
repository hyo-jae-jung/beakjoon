from sys import stdin 

N,game = stdin.readline().strip().split()
games = {'Y':1,'F':2,'O':3}
players = set()
for _ in range(int(N)):
    players.add(stdin.readline().strip())

print(len(players)//games[game])
