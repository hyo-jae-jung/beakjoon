from sys import stdin  

data = {
"Algorithm":"204",
"DataAnalysis":"207",
"ArtificialIntelligence":"302",
"CyberSecurity":"B101",
"Network":"303",
"Startup":"501",
"TestStrategy":"105",
}

N = int(stdin.readline().strip())

ans = []
for _ in range(N):
    ans.append(data[stdin.readline().strip()])

print(*ans,sep='\n')
