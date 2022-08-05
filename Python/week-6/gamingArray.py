#
# Complete the 'gamingArray' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def gamingArray(arr):
    # Write your code here
    count_max = 0
    last_max = 0
    for a in arr:
        if a > last_max: 
            last_max = a
            count_max +=1
    return 'ANDY' if count_max % 2 == 0 else 'BOB'

if __name__ == '__main__':
    g = int(input().strip())

    for g_itr in range(g):
        arr_count = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = gamingArray(arr)

        print(f'Result: {result}')

