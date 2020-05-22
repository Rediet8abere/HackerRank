def substrCount(s):
    # geeks for geeks
    n = len(s)
    result = 0
    char_count_list = [0]*n
    i = 0
    while i < n:
        char_count = 1
        j = i + 1
        while j < n:
            if s[i] != s[j]:
                break
            char_count += 1
            j += 1
        result += int((char_count * (char_count+1))/2)
        char_count_list[i] = char_count
        i = j

    for i in range(1, n):
        if s[i-1] == s[i]:
            char_count_list[i] = char_count_list[i-1]
        if i < (n-1) and s[i-1] == s[i+1] and s[i] != s[i+1]:
            if char_count_list[i-1] < char_count_list[i+1]:
                result += char_count_list[i-1]
            else:
                result += char_count_list[i+1]
    return result




print(substrCount("aaaa"))
