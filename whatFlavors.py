def whatFlavors(cost, money):
    sorted_cost = sorted(cost)
    left = 0
    right = len(sorted_cost)-1
    # 1, 2, 3, 4, 5
    flavour = []
    while left < right:
        sumF = sorted_cost[left] + sorted_cost[right]
        if sumF == money:
            flavour.append(sorted_cost[left])
            flavour.append(sorted_cost[right])
            break
        elif sumF < money:
            left += 1
        elif sumF > money:
            right -= 1
    indices = []
    for i in range(len(cost)):
        if flavour[0] == cost[i]:
            print("0=>", cost[i], i+1)
            indices.append(i+1)
        elif flavour[1] == cost[i]:
            print("1=>", cost[i], i+1)
            indices.append(i+1)
    print(indices[0], indices[1])


whatFlavors([4, 3, 2, 5, 7], 8)
