#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    # Write your code here
    max_len = 0
    counters = [0] * 101
    for i in range(len(a)):
        counters[a[i]] += 1
    
    for i in range(len(counters) - 1):
        length = counters[i + 1] + counters[i]

        if length > max_len:
            max_len = length

    return(max_len)

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    print(f'Result: {result}')
