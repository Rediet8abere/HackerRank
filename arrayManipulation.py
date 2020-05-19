def arrayManipulation(n, queries):
    arr = [0]*n
    for i in range(len(queries)):
        arr[queries[i][0]-1] += queries[i][2]
        if queries[i][1] < len(arr):
            arr[queries[i][1]] -= queries[i][2]
    sum = 0
    max = 0
    for i in range(len(arr)):
        sum += arr[i]
        if sum > max:
            max = sum
    return max
arrayManipulation(5, [[1, 2, 100], [2, 5, 100], [3, 4, 100]])
