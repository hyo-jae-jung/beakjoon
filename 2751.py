N = int(input())
M = [int(input()) for _ in range(N)]
def quick_sort2(array):
    if len(array)<=1: return array
    pivot=array[0]
    tail=array[1:] # list excludes the pivot
    left_=[x for x in tail if x<=pivot] # left divided part
    right_=[x for x in tail if x>pivot] # right divided part
    return quick_sort2(left_)+[pivot]+quick_sort2(right_)

for i in quick_sort2(M):
    print(i)
    