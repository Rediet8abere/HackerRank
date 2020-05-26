def MaximumSubarray(arr):
    max_sum = float('-inf')
    current_sum = 0
    for num in arr:
        current_sum = max(num, current_sum+num)
        max_sum = max(max_sum, current_sum)
    print(max_sum)
    # -2, 1, -3, 4, -1, 2, 1, -5, 4
    #                             ^
    # max_sum = 6
    # current_sum = 5


MaximumSubarray([-2,1,-3,4,-1,2,1,-5,4])
