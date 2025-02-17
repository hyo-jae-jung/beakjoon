from sys import stdin   

arr = [5,7,9,0,3,1,6,2,4,8]

def pivoting(a):
    arr = a
    print(arr)
    pivot = arr[0]
    i = 1
    j = len(arr)-1

    while i < j:
        while arr[i] < pivot:
            i+=1

        while arr[j] > pivot:
            j-=1

        if i < j:
            arr[i],arr[j] = arr[j], arr[i]    
            i+=1
            j-=1
    else:
        arr[0],arr[j] = arr[j],arr[0]
        print(arr)
        pivoting(arr[j+1:])
        pivoting(arr[:j])

pivoting(arr)
print(arr)

