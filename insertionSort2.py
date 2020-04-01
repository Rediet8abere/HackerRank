def insertionSort2(n, arr):
    # 3 4 7 5 6 2 1
    for i in range(n):
        key=arr[i]
        j=i-1
        while j>=0 and key<arr[j]:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
        if i>0:
            print(*arr)


insertionSort2(7, [3, 4, 7, 5, 6, 2, 1])
