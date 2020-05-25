def commonChild(s1, s2, n, m):
    n = len(s1)
    m = len(s2)
    w, h = n+1, m
    Matrix = [[0 for x in range(w)] for y in range(h)]
    for i in range(n):
        for j in range(m):
            if s1[i] == s2[j]:
                Matrix[i][j] = 1 + Matrix[i-1][j-1]
            else:
                Matrix[i][j] = max(Matrix[i-1][j], Matrix[i][j-1])
    return Matrix[m-1][n-1]




s1 = "WEWOUCUIDGCGTRMEZEPXZFEJWISRSBBSYXAYDFEJJDLEBVHHKS"
s2 = "FDAGCXGKCTKWNECHMRXZWMLRYUCOCZHJRRJBOAJOQJZZVUYXIC"
n = len(s1)
m = len(s2)
print(commonChild(s1, s2, n, m))
