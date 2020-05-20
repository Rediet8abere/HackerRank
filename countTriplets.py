def countTriplets(arr, r):
    init_arr_count = {}
    seen_ele = {}
    count_triplets = 0
    # 1, 5, 5, 25, 125
    #               ^
    # 5

    # init = {1:1, 5:0, 25:0, 125:0}
    # seen = {1:1, 5:2, }
    # count_triplets = 1*1 = 1
    #                = 1*1 = 1
    #                = 2*1 = 2
    #                =
    for i in range(len(arr)):
        if arr[i] not in init_arr_count:
            init_arr_count[arr[i]] = 1
        elif arr[i] in init_arr_count:
            init_arr_count[arr[i]] += 1

    for i in range(len(arr)):
        init_arr_count[arr[i]] -= 1
        if arr[i]/r in seen_ele and arr[i]%r == 0:
            if arr[i]*r in init_arr_count:
                count_triplets += init_arr_count[arr[i]*r]*seen_ele[int(arr[i]/r)]
            # a pair exists
            # print(count_triplets, int(arr[i]/r), arr[i]*r)
        if arr[i] not in seen_ele:
            seen_ele[arr[i]] = 1
        elif arr[i] in seen_ele:
            seen_ele[arr[i]] += 1


    print(count_triplets)



countTriplets([1, 5, 5, 25, 125], 5)
