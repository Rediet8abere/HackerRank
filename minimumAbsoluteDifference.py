def minimumAbsoluteDifference(arr):
    min_diff = float('inf')
    sorted_arr = sorted(arr)
    list = []
    for i in range(1, len(sorted_arr)):
        abs_dist = abs(sorted_arr[i] - sorted_arr[i-1])
        if abs_dist < min_diff:
            min_diff = abs_dist
            list.append(abs_dist)
    return min_diff



print(minimumAbsoluteDifference([-59, -36, -13, 1, -53, -92, -2, -96, -54, 75]))
