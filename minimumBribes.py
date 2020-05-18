def minimumBribes(q):
    count = 0
    for i in range(len(q)-1, -1, -1):
        if q[i] != i+1:

            if q[i-2] == (i+1):
                count += 2
                q[i], q[i-2] = q[i-2], q[i]
                q[i-2], q[i-1] = q[i-1], q[i-2]
            elif q[i-1] == (i+1):
                count += 1
                q[i], q[i-1] = q[i-1], q[i]
            elif q[i] - (i+1) > 2:
                print("Too chaotic")
                return
    print(count)
minimumBribes([1, 2, 5, 3, 7, 8, 6, 4])
