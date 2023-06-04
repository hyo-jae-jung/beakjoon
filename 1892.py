from sys import stdin 
from math import factorial as f
from fractions import Fraction

N,K = map(int,stdin.readline().strip().split())

answer = Fraction(f(N)*(2**(N-K)),(f(K)*f(N-K))*(3**N))

print(answer.numerator,answer.denominator)
