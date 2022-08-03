#
# Complete the 'icecreamParlor' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER m
#  2. INTEGER_ARRAY arr
#

def icecreamParlor(m, arr):
    # Write your code here
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            print(f'Indexes: i={i}, j={j}')
            print(f'Sum: {arr[i] + arr[j]}')

            if i >= j:
                continue

            if arr[i] + arr[j] == m:
                res = [i + 1, j + 1]
                res.sort()
                return res

if __name__ == '__main__':
    # t = int(input().strip())

    # for t_itr in range(t):
    #     m = int(input().strip())
    #     n = int(input().strip())
    #     arr = list(map(int, input().rstrip().split()))

    m = 4
    # arr = [1, 4, 5, 3, 2]
    arr = [2, 2, 4, 3]

    result = icecreamParlor(m, arr)

    print(f'Result: {result}')
