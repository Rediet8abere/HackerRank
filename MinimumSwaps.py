def minimumSwaps(arr):
    """ Time-Complexity: O(n*m) where n is the outer loop
    and m is innter loop.
    """
    swap_count = 0
    for i in range(len(arr)):
        while arr[i] != (i+1):
            swap_item_index = arr[i]-1
            temp = arr[i]
            arr[i] = arr[swap_item_index]
            arr[swap_item_index] = temp
            swap_count += 1

    print(swap_count)
    print(arr)
minimumSwaps([7, 1, 3, 2, 4, 5, 6])
# 6, 1, 3, 2, 4, 5, 7   1
# 5, 1, 3, 2, 4, 6, 7   2
# 4, 1, 3, 2, 5, 6, 7   3
# 2, 1, 3, 4, 5, 6, 7   4
# 1, 2, 3, 4, 5, 6, 7   5
