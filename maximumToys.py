def maximumToys(prices, k):
    for i in range(len(prices)):
        min = i
        for j in range(i, len(prices)):
            if prices[j] < prices[min]:
                min = j
        temp = prices[i]
        prices[i] = prices[min]
        prices[min] = temp
    print("sorted price: ", prices)
    sum = 0
    count  = 0
    for i in range(len(prices)):
        sum += prices[i]
        if sum <= k:
            count += 1
        else:
            break
    print("count: ", count)
    return count


maximumToys([1, 12, 5, 111, 200, 1000, 10], 50)
# 13, 14, 0, 3, 1, 8
# 0, 14, 13, 3, 1, 8
# 0, 13, 14, 3, 1, 8
# 0, 3, 14, 13, 1, 8
# 0, 1, 14, 13, 3, 8
