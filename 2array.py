# """
# # arr1 = [3, 1, 6, 9, 10]
# # arr1 = [1, 3, 6, 9, 10]
#
# # arr2 = [7, 4, 0, 1, 5]
# # arr2 = [0, 1, 4, 5, 7]
#
# # prev =
# # cur =
#
# t = 8
#
# """
#
# def twoarray(arr1, arr2, t):
#     pointer1 = 0
#     pointer2 = 0
#     cur = []
#     while pointer1 < len(arr1) and pointer2 < len(arr2):
#         if arr1[pointer1] + arr2[pointer2] > t:
#             cur.append()
#
#
# twoarray([1, 3, 6, 9, 10], [0, 1, 4, 5, 7], 8)




"""
1 - > 3 -> 8 -> 2
1 < - 3 < - 8 < - 2
2 - > 8 -> 3 - > 1



"""
# data next
# def reverse(ll):
#     cur_node = ll.head
#     prev = None
#     while cur_node.next != None:
#         next = cur_node.next
#         cur_node.next = prev
#         prev = cur_node
#         cur_node = next
# reverse()


"""find smallest and second smallest
smallest = []
min = arr[0]
for i in range(1, len(arr)):
    if arr[i] < min:
        min = arr[i]

"""
