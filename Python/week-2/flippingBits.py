#
# Complete the 'flippingBits' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#

def flippingBits(n):
    # Write your code here
    s = f'{n:032b}'
    res = ''
    for i in s:
        if i == '0':
            res += '1'
        elif i == '1':
            res += '0'

    return int(res, 2)

if __name__ == '__main__':
    # q = int(input().strip())

    # for q_itr in range(q):
    #     n = int(input().strip())

    q = [2147483647, 1, 0]

    for n in q:
        result = flippingBits(n)

        print(f'Got Result: {result}')
