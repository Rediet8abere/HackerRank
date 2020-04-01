"""Given a sorted list with an unsorted number  in the rightmost cell,
can you write some simple code to insert  into the array so that it remains sorted?

        1. Restate the problem: Every element in the array is sorted excpet
                                for the last element, then what my function needs
                                to do is take that array and put the last element
                                in it's place so that the whole array is sorted.
        2. Ask clarifying question: Are all elements in the array positive integers?,
                                    Can the list be empty or null?, and can I expect
                                    only one unsorted element in the array or can it be
                                    more than one?
        3. Assumption: I would assume all elements are positive integers and there is
                       only one unsorted element in the rightmost cell for simplicity
                       sake input: [1, 3, 4, 5, 2] 5 output: [1, 2, 3, 4, 5]
        4. Brain storming solution: The way I would solve it would be...... I would start
                                    looping through the list and store the last element in a
                                    variable let's call it key, store the index before the last one
                                    in a variable let's call it j and I would start comparing the
                                    key to the element at index j. If it is less than element at index
                                    j then the element at index j would take the place of the key
                                    leaving it's duplicate in it's original place and substract 1 from j
                                    to allow us moving up the list. we would repeat this step creating a duplicate
                                    of j at index len(arr)-(i+1) until there is nolonger a number that is less than the key.
        5. Trade-offs: Since we will be using two loops to keep track of where we are in the loop and find the right place
                       for our element out time-complexity=> adds up to O(n)^2 and the only space we use to run our function
                       is for key and j space-complexity: O(1)+O(1)~O(1)
       6. Improvements: The question itself askes for a brute force solution; therefore I would stick with my solution
 # in
"""

# [1, 3, 4, 5, 2]


def insertionSort1(n, arr):

    for i in range(n):
        key=arr[n-1]
        j = n-2
        while key<arr[j] and j>=0:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
    print("arr: ", arr)
insertionSort1(5, [1, 3, 4, 5, 2])
