""" 1. Restate the problem: My function takes an integer as an input and prints
                            out a staircase using a hash char and spaces.
    2. Ask clarifying question: are the integers only positive?
    3. Think out loud: Looks like a for loop problem, since we have height and width
                      we have to keep track of the x and y direction using i and j from
                      loop.
    4. Trade offs: Two loops mean O(n)^2 for print we have O(n) for every charater printed.
"""

def staircase(n):

    # for i in range(1, n+1):
    #     print(str('#'*i).rjust(n))
    for i in range(1, n+1):
        j = n-i
        while j>=0:
            print(str(' '), end='')
            j-=1
        print(str('#'*i))

# (1, 3)
# (2, 2)
staircase(6)
"""
   #
  ##
 ###
####
"""
