def isValid(s):
    str_dict = {}
    for char in s:
        if char not in str_dict:
            str_dict[char] = 1
        elif char in str_dict:
            str_dict[char] += 1
    max_count = str_dict[char]
    min_count = str_dict[char]
    count_occur = {}
    for key, value in str_dict.items():
        if value in count_occur:
            count_occur[value] += 1
        else:
            count_occur[value] = 1
        if value > max_count:
            max_count = value
        if value < min_count:
            min_count = value
    if len(count_occur) == 1:
        return "YES"
    elif len(count_occur) == 2:
        if count_occur[max_count] == 1 and max_count - min_count == 1:
            return "YES"
        elif count_occur[min_count] == 1 and min_count == 1:
            return "YES"
    return "NO"


# [1, 1, 1, 2, 2, 2]
# true or flase = true
print(isValid("aabbbc"))
