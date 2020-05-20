class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def comparator(a, b):
            if a.score < b.score:
                return 1
            elif a.score == b.score:
                if a.name.lower() == b.name.lower():
                    return 0
                elif a.name.lower() > b.name.lower():
                    return 1
                else:
                    return -1
            else:
                return -1
