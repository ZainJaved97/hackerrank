import math
import os
import random
import re
import sys

#
# Complete the 'divisibleSumPairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER_ARRAY ar
#

def divisibleSumPairs(n, k, ar):
    rest = [0] * k
    nrOfPairs = 0
    for elem in ar:
        nrOfPairs += rest[(k - elem % k) % k]
        rest[elem % k] += 1

        print(f"Rest: {rest}")
        print(f"Pairs: {nrOfPairs}")
    return nrOfPairs

    # Write your code here
    # r = [0] * k
    # for i in range(len(ar)):
    #     r[int(ar[i]%k)] += 1

    # count = (r[0]*(r[0]-1))/2

    # if k%2==0 and k>=2:
    #     count = count + (r[int(k/2)]*(r[int(k/2)]-1))/2
    #     for i in range(1,int((k/2))):
    #         count = count + r[i]*r[k-i]
    # else:
    #     for i in range(1,int((k+1)/2)):
    #         count = count + r[i]*r[k-i]
    # return int(count)


# def divisibleSumPairs(n, k, ar):
#     # n, k = 6, 3
#     # ar = [1, 3, 2, 6, 1, 2]

#     count = 0
#     for outer_index, outer_number in enumerate(ar):
#         # print(f"Outer Index: {outer_index}, Outer Number: {outer_number}")
#         for inner_index, inner_number in enumerate(ar[:]):
#             # print(f"Inner Index: {inner_index}, Inner Number: {inner_number}")

#             # print(f"Outer Number: {outer_number}, Inner Number: {inner_number}, Sum: {outer_number + inner_number}\n\n\n")

#             if outer_index > inner_index or outer_number == inner_number:
#                 continue

#             if (outer_number + inner_number) % k == 0:
#                 count += 1
#                 # print(f"Count: {count}\n\n\n")
#                 # print("~" * 50)
#                 # print(f"Outer Number: {outer_number}, Inner Number: {inner_number}")
#                 print(f"Outer Index: {outer_index}, Inner Index: {inner_index}")
#                 print("~" * 50)
#                 print("\n\n\n")

#     return count


if __name__ == '__main__':
    # first_multiple_input = input().rstrip().split()

    # n = int(first_multiple_input[0])
    # k = int(first_multiple_input[1])
    # ar = list(map(int, input().rstrip().split()))

    # n, k = 6, 5
    # ar = [1, 2, 3, 4, 5, 6]
    n, k = 6, 3
    ar = [1, 3, 2, 6, 1, 2]

    result = divisibleSumPairs(n, k, ar)

    print(f"Result: {result}")
