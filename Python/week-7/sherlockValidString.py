from collections import Counter

#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isValid(s):
    # Write your code here
    count = Counter(s)
    s = sorted(count.values())

    yes = len(set(s)) == 1

    if yes:
        return 'YES'
    elif len(set(s[:-1] + [s[-1] - 1])) == 1:
        return 'YES'
    elif len(set([n for n in [s[0] - 1] + s[1:] if n > 0])) == 1:
        return 'YES'

    return 'NO'

if __name__ == '__main__':
    s = input()

    result = isValid(s)

    print(f'Result: {result}')

