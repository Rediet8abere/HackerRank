def rotLeft(a, d):
    for i in range(d):
        rot = a.pop(0)
        a.append(rot)
    return a

print(rotLeft([1, 2, 3, 4, 5], 2))
