#
# Complete the 'marsExploration' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def marsExploration(s):
    # Write your code here
    count = 0
    for i in range(0, len(s), 3):
        if s[i] != 'S':
            count += 1
        if s[i+1] != 'O':
            count += 1
        if s[i+2] != 'S':
            count += 1

    return count

if __name__ == '__main__':
    # s = input()

    s = 'SOSSOTSES'

    result = marsExploration(s)

    print(f'Got Result: {result}')
