#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # Write your code here

    sea_level = 0
    valley_count = 0

    for step in path:
        if step == 'U':
            sea_level += 1
            if sea_level == 0:
                valley_count += 1

        elif step == 'D':
            sea_level -= 1

    return valley_count


if __name__ == '__main__':
    # steps = int(input().strip())

    # path = input()

    # steps = 8
    # path = 'UDDDUDUU'
    steps = 12
    path = 'DDUUDDUDUUUD'

    result = countingValleys(steps, path)

    print(f'Got Result: {result}')
