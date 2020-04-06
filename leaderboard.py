def leaderboard(scores, alice):
    rankNum = 1
    rank = []
    prev_score = 0
    for i in range(len(scores)):
        if scores[i] != prev_score:
            rank.append(rankNum)
            prev_score = scores[i]
            rankNum += 1
        elif scores[i] == prev_score:
            rank.append(rank[len(rank)-1])
    print("rank: ", rank)
    alice_rank = []
    for i in range(len(alice)):
        if alice[i] > scores[0]:
            alice_rank.append(rank[0])
        elif alice[i] < scores[len(scores)-1]:
            alice_rank.append(rank[len(scores)-1]+1)
        else:
            mid = len(scores)//2
            low = 1
            high = len(scores)-2
            while low < high:
                if alice[i] == scores[mid]:
                    alice_rank.append(rank[mid])
                    break
                elif alice[i] > scores[mid]:
                    high = mid - 1

                else:
                    low = mid + 1
                mid = (low+high)//2
            if low >= high:
                print("mid: ", mid, alice[i], scores[mid])
                if alice[i] < scores[mid]:
                    alice_rank.append(rank[mid+1])
                else:
                    alice_rank.append(rank[mid])
    print("alice_rank: ", alice_rank)
    for ele in alice_rank:
        print(ele)

leaderboard([100, 90, 90, 90, 80, 75, 60], [50, 65, 77, 90, 102])
