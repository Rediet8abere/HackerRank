def checkMagazine(magazine, note):
    # construct a dict for maga with count
    # compare note with dict
    maga_dict = {}
    for i in range(len(magazine)):
        if magazine[i] not in maga_dict:
            maga_dict[magazine[i]] = 1
        else:
            maga_dict[magazine[i]] += 1
    for i in range(len(note)):
        if note[i] in maga_dict:
            maga_dict[note[i]] -= 1
        else:
            print("No")
            return
        if maga_dict[note[i]] == 0:
            del maga_dict[note[i]]
    print("Yes")
checkMagazine(["two", "times", "three", "is", "not", "four"], ["two", "times", "two" "is", "four"])
