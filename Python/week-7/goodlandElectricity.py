#
# Complete the 'pylons' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

def pylons(k, arr):
    # Write your code here
    n = len(arr)
    out = 0
    prev, curr = -k, -k 
    for i in range(n):
        if i - curr >= 2*k:
            return -1
        if arr[i]:
            if i - prev >= 2 * k:
                prev = curr
                out += 1
            curr = i
                
    return out + 1

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = pylons(k, arr)

    print(f'Result: {result}')

