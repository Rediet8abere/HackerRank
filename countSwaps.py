def countSwaps(a):
    swaps = 0
    for i in range(len(a)-1):
        for j in range(len(a)-1):
            if a[j] > a[j+1]:
                swaps += 1
                temp = a[j]
                a[j] = a[j+1]
                a[j+1] = temp
    return swaps, a[0], a[len(a)-1]

print("result: ", countSwaps([3, 2, 1]))
