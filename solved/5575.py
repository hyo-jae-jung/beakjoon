from sys import stdin 
from datetime import datetime

h_a1,m_a1,s_a1,h_a2,m_a2,s_a2 = map(int,stdin.readline().strip().split())
h_b1,m_b1,s_b1,h_b2,m_b2,s_b2 = map(int,stdin.readline().strip().split())
h_c1,m_c1,s_c1,h_c2,m_c2,s_c2 = map(int,stdin.readline().strip().split())

print(*list(map(int,str((datetime(2024,4,8,h_a2,m_a2,s_a2) - datetime(2024,4,8,h_a1,m_a1,s_a1))).split(':'))))
print(*list(map(int,str((datetime(2024,4,8,h_b2,m_b2,s_b2) - datetime(2024,4,8,h_b1,m_b1,s_b1))).split(':'))))
print(*list(map(int,str((datetime(2024,4,8,h_c2,m_c2,s_c2) - datetime(2024,4,8,h_c1,m_c1,s_c1))).split(':'))))
