def stepPerms(n):
    # memo = {}
    # if n < 0:
    #     return 0
    # if n == 1 or n == 0:
    #     return 1
    # if n not in memo:
    #     memo[n] = stepPerms(n-1) + stepPerms(n-2) + stepPerms(n-3)
    #     return memo[n]
    # else:
    #     return memo[n]

    arr = [i for i in range(n+1)]
    arr[0] = 1
    arr[1] = 1
    arr[2] = 2
    for i in range(3, n+1):
        # print("hello", i)
        arr[i] = arr[i-1] + arr[i-2] +  arr[i-3]
    return arr[n]
print("steps: ", stepPerms(3))
# 1 1 1
# 1 2
# 2 1
# 3
