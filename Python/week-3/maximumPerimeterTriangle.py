#
# Complete the 'maximumPerimeterTriangle' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY sticks as parameter.
#

def maximumPerimeterTriangle(sticks):
    # Write your code here
    sticks = sorted(sticks, reverse=True)

    for i in range(0, len(sticks) - 2):
        if sticks[i] < sticks[i + 1] + sticks[i + 2]:
            return [sticks[i + 2], sticks[i + 1], sticks[i]]

    return [-1]

if __name__ == '__main__':
    n = int(input().strip())

    sticks = list(map(int, input().rstrip().split()))

    result = maximumPerimeterTriangle(sticks)

    print(f'Result: {result}')
