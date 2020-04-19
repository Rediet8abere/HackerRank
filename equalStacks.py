h1 = [3, 2, 1, 1, 1]
h2 = []
h3 = [1, 1, 4, 1]

def equalStacks(h1, h2, h3):
    h1_Stack = []
    h2_Stack = []
    h3_Stack = []
    h1_sum = 0
    for i in range(1, len(h1)+1):
        h1_sum += h1[len(h1)-i]
        h1_Stack.append(h1_sum)
    h2_sum = 0
    for i in range(1, len(h2)+1):
        h2_sum += h2[len(h2)-i]
        h2_Stack.append(h2_sum)
    h3_sum = 0
    for i in range(1, len(h3)+1):
        h3_sum += h3[len(h3)-i]
        h3_Stack.append(h3_sum)
    print("stack: ", h1_Stack, h2_Stack, h3_Stack)
    i = len(h1)-1
    j = len(h2)-1
    k = len(h3)-1
    if len(h1) == 0 or len(h2) == 0 or len(h3) == 0:
        return 0
    while i >= 0 and j >= 0 and k >= 0:
        if h1_Stack[i] == h2_Stack[j] and h2_Stack[j] == h3_Stack[k]:
            return h1_Stack[i]
        elif h1_Stack[i] > h2_Stack[j] and h1_Stack[i] > h3_Stack[k]:
            h1_Stack.pop()
            i -= 1
        elif h2_Stack[j] > h1_Stack[i] and h2_Stack[j] > h3_Stack[j]:
            h2_Stack.pop()
            j -= 1
        elif h3_Stack[k] > h1_Stack[i] and h3_Stack[k] > h2_Stack[j]:
            h3_Stack.pop()
            k -= 1
    # return h1_Stack[i]
print(":", equalStacks(h1, h2, h3))
