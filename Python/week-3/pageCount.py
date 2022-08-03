#
# Complete the 'pageCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER p
#

from math import ceil, floor


def pageCount(n, p):
    # Write your code here
    return min(p//2, n//2 - p//2)

if __name__ == '__main__':
    n = int(input().strip())
    p = int(input().strip())

    # n = 5
    # p = 4

    result = pageCount(n, p)

    print(f'Result: {result}')
