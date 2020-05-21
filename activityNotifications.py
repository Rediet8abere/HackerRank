def getMedian(counting_sort, median_index, d):
    counter, left = 0, 0
    # 10, 20, 30, 40, 50
    # 2, 2, 3, 3, 4

    # median_index: 2
    # counter: 1
    # left: 11
    # 10, 20, 30
    # [0, 0]
    print("median_index: ", median_index)

    while counter < median_index:
        # print(counter, left)
        counter += counting_sort[left]
        left += 1
    # print("left: ", left)
    # right: 4
    # left: 3
    right = left
    left -= 1
    if counter > median_index or d % 2 != 0:
        # print("left", left)
        return left
    else:
        while counting_sort[right] == 0:
            right += 1
        return (right+left)/2

def activityNotifications(expenditure, d):
    # couting sort
    counting_sort = [0]*201
    # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    # start sorting with the first d elements
    # 2, 3, 4, 2, 3
    for i in range(d):
        counting_sort[expenditure[i]] += 1
    # print(counting_sort)
    # d+((len(expenditure)-d) * (d/2 + d/2))
    # determine the median
    # 2, 2, 3, 3, 4
    if d % 2 == 0:
        median_index = int(d/2)
    else:
        median_index = int(d/2)+1
    start = 0
    end = d
    notification_count = 0
    while end < len(expenditure):
        median = getMedian(counting_sort, median_index, d)
        print(median)
        if expenditure[end] >= 2*median:
            notification_count += 1
        counting_sort[expenditure[start]] -= 1
        counting_sort[expenditure[end]] += 1
        start += 1
        end += 1
        # print(counting_sort)
    print(notification_count)
    # [0, 0, 1, 1, 2]

activityNotifications([10, 20, 30, 40, 50], 3)
