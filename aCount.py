def probInd(ne, ele, ind):

    ele = ele.split()
    print("ele: ", ele)
    indices = set()
    for i in range(ne):
        if ele[i] == 'a':
            print("ele", ele[i], 'i', i)
            indices.add(i+1)
    print("indices: ", indices)
    possTup = []
    count = 0
    num = 0
    for i in range(1, ne):
        j = i+1
        loop = ne-i
        while loop>0:
            possTup.append((i, j))
            j += 1
            loop-=1
            count += 1
            if i in indices or j in indices:
                print(i, j)
                num += 1
    num += 1

    print("count: ", count, "num: ", num)
    print("possTup: ", possTup)
    print(num/count)

    # from itertools import combinations
    # # ne, ele, ind
    # # ne,ele,ind = input(),input().split(),int(input())
    # t = list(combinations(ele,ind))
    # print("t: ", t)
    # f = [i for i in t if 'a' in i]
    # print(len(f)/len(t))

probInd(9, 'a b c a d b z e o', 4)

# 0.722222222222
