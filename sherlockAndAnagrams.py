import string
def sherlockAndAnagrams(s):
    # ALPHABET = string.ascii_lowercase
    # seen_char_count = [0]*len(ALPHABET)
    # substring = {}
    # for letter in s:
    #     seen_char_count[ord(letter)-ord('a')] += 1
    # # print(seen_char_count)
    #
    # for i in range(len(s)):
    #     for j in range(i, len(s)):
    #         seen_char_count = [0] * len(ALPHABET)
    #         print(s[i:j+1])
    #         for letter in s[i:j+1]:
    #             seen_char_count[ord(letter)-ord('a')] += 1
    #             # print(ord(letter)-ord('a'))
    #
    #         seen_char_count = tuple(seen_char_count)
    #         # print(seen_char_count)
    #         substring[seen_char_count] = substring.get(seen_char_count, 0) + 1
    # print(substring)

    substring = {}
    n = len(s)
    for i in range(n):
        for j in range(n):
            # print(s[i:j+1])
            sorted_sub = ''.join(sorted(s[i:j+1]))
            if sorted_sub not in substring and sorted_sub != '':
                substring[sorted_sub] = 1
            elif sorted_sub in substring:
                substring[sorted_sub] += 1
    print(substring)
    count = 0
    for occurance in substring.values():
        # 4*1.5 = 6.0
        # 3*1 = 3
        # 2*0.5 = 1
        count += occurance * (occurance-1)/2
    print(int(count))



sherlockAndAnagrams("kkkk")
