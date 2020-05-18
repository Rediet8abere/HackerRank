def crosswordPuzzle(crossword, words):
    print("words: ", words)
    for word in words:
        print("word: ", len(word))
    x = 0
    y = 0
    for i in range(len(crossword)):
        for j in range(len(crossword[i])):
            if crossword[i][j] == '-':
                count = 1
                words[x][y]
                pass
    return crossword


def recursive(count, words, crossword, i, j):
    if count == len(words):
        pass
    if i < 0 or i >= len(crossword) or j < 0 or j >= len(crossword[i]) or crossword[i][j] == '+':
        return

    crossword[i][j] = words[i][j]



crossword = ["+-++++++++",
             "+-++++++++",
             "+-++++++++",
             "+-----++++",
             "+-+++-++++",
             "+-+++-++++",
             "+++++-++++",
             "++------++",
             "+++++-++++",
             "+++++-++++"]

words = "LONDON;DELHI;ICELAND;ANKARA"
crosswordPuzzle(crossword, words.split(';'))

def nextSquare():
    i = 1;

    # An Infinite loop to generate squares
    while True:
        yield i*i
        i += 1  # Next execution resumes
                # from this point

# Driver code to test above generator
# function
for num in nextSquare():
    if num > 100:
         break
    print(num)
