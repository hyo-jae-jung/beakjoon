##############################
eval() exec()
##############################
exec("x = a / b")
x

>>> 2.0

##############################

x = eval("a / b")
x

>>> 2.0
##############################


input()보다
sys.stdin.readline()가 더 빠름 왜?
input()은 prompt message 기능도 있어서 일을 더 함.

##############################

(A,B최대공약수)= A*B/(A,B최소공배수)
최소공배수는 유클리드 호제법으로 구해야 시간복잡도를 O(logN)으로
줄일 수 있다.

##############################

에라토스테네스의 체

컨셉은 알겠는데 문제에 많이 나오니 숙련도를 높여야 겠다..

###############################
itertools에 permutations, combinations는 잘 쓰고 있는데
얘네는 중복허용 안함. 중복허용(복원추출)하려면
product, combinations_with_replacement를 사용해야함

https://docs.python.org/ko/3/library/itertools.html?highlight=product#module-itertools

이렇게 4개가 조합형 이터레이터의 전부

itertools에 진작에 알았으면 좋았을 다양한 기능이 있다.
cycle, accumulate, ...
써보자.
###############################

functools라는거도 있다..

###############################

dict.fromkeys(key_list,value(단일원소))
ex) dict.fromkeys([1,2,3,4,5],0)
-->{1: 0, 2: 0, 3: 0, 4: 0, 5: 0}

##################################

최대공약수 : math.gcd  
최소공배수 : math.lcm  (python3.9 이상에서 사용 가능)

##################################

이분탐색 라이브러리 및 함수  

from bisect import bisect_left, bisect_right  

def cnt_within_range(arr, left_v, right_v):  
    left_idx = bisect_left(arr, left_v)  
    right_idx = bisect_right(arr, right_v)  
    return right_idx - left_idx  

이분탐색으로 원소 개수 찾으면 시간복잡도 O(logn)이라 더 빠름  

##################################

Pascal's rule  
nCk + nC(k+1) = (n+1)C(k+1)  
