def hanoi(n, start, end, stopover):
    if n == 1:
        print(start, '->', end)
    else:
        hanoi(n-1, start, stopover, end)
        print(start, '->', end)
        hanoi(n-1, stopover, end, start)

hanoi(3,1,3,2)
