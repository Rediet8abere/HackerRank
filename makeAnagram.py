def makeAnagram(a, b):
    a_dict = {}
    for i in range(len(a)):
        if a[i] not in a_dict:
            a_dict[a[i]] = 1
        else:
            a_dict[a[i]] += 1
    b_dict = {}
    for i in range(len(b)):
        if b[i] not in b_dict:
            b_dict[b[i]] = 1
        else:
            b_dict[b[i]] += 1
    # print(a_dict)
    # print(b_dict)
    deletion_count = 0
    for i in range(len(a)):
        if a[i] not in b_dict:
            deletion_count += 1
        elif a[i] in b_dict:
            b_dict[a[i]] -= 1
            if b_dict[a[i]] == 0:
                del b_dict[a[i]]
    for i in range(len(b)):
        if b[i] not in a_dict:
            deletion_count += 1
        elif b[i] in a_dict:
            a_dict[b[i]] -= 1
            if a_dict[b[i]] == 0:
                del a_dict[b[i]]
    print(deletion_count)
makeAnagram("cde", "abc")
