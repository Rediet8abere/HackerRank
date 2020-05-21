def alternatingCharacters(s):
    minimum_deletion_count = 0
    for i in range(1, len(s)):
        if s[i-1] == s[i]:
            minimum_deletion_count += 1
    print(minimum_deletion_count)
alternatingCharacters("AAABBB")
