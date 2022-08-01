#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here

    count = len(arr)

    ltr_sum = 0
    rtl_sum = 0

    for i in range(count):
        ltr_sum += arr[i][i]
        rtl_sum += arr[count - i -1][i]

    return abs(ltr_sum - rtl_sum)

if __name__ == '__main__':
    # n = int(input().strip())

    arr = [
        [11, 2, 4], 
        [4, 5, 6],
        [10, 8, -12]
    ]

    # for _ in range(n):
    #     arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    print(f'Result: {result}')
