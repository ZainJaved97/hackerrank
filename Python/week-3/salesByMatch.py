#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    # Write your code here
    d = {}
    pairs = 0
    for i in ar:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
            if d[i] % 2 == 0:
                pairs += 1

    return pairs

if __name__ == '__main__':
    # n = int(input().strip())

    # ar = list(map(int, input().rstrip().split()))
    n = 7
    ar = [1, 2, 1, 2, 1, 3, 2]

    result = sockMerchant(n, ar)

    print(f'Result: {result}')
