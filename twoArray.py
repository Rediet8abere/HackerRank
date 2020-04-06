""" Given two list check if the list contains the identical elements.
    1. Assumptions: I would assume the list is [1, 3] and [2, 2]
"""
def twoArray(list1, list2):
    list1_dic = {}
    for i in range(len(list1)):
        if list1[i] not in list1_dic:
            list1_dic[list1[i]] = 1
        else:
            list1_dic[list1[i]] += 1

    list2_dic = {}
    for i in range(len(list2)):
        if list2[i] not in list2_dic:
            list2_dic[list2[i]] = 1
        else:
            list2_dic[list2[i]] += 1
    print("list1_dic: ", list1_dic)
    print("list2_dic: ", list2_dic)
    return list1_dic == list2_dic
print(twoArray(['a', 1, 3, 2, 2, 1], [1, 1, 2, 2, 'a', 3]))
