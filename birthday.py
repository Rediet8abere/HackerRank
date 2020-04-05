def birthdayCakeCandles(ar):
    max = 0
    count = 0
    for i in range(len(ar)):
        if ar[i] > max:
            max = ar[i]

    for i in range(len(ar)):
        if ar[i] == max:
            count += 1
    print("count: ", count)
    return count

birthdayCakeCandles([4, 4, 2, 1])
