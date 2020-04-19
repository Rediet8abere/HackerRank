""" Given a large number of ints, return the largest possible product of 3 numbers.
"""
[1, 4, 2, 9]
# - - + = +
#  - + + = -
#  - - - = -
def largestProduct(arr):
    arr = sorted(arr)
    product1 = arr[len(arr)-1] * arr[len(arr)-2] * arr[len(arr)-3]
    product2 = arr[0] * arr[1] * arr[len(arr)-1]
    if product1 > product2:
        return product1
    else:
        return product2


print(largestProduct([10, 3, 4, 1, 5]))
