#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a):
    # Write your code here
    
    # Solution 1
    for i in a:
        c = a.count(i)
        if c == 1:
            return i

    # Solution 2
    # unique=0
    # for i in a:
    #     unique^= i
    # return unique

    # Solution 3
    # return 2*sum(set(a)) - sum(a)


if __name__ == '__main__':
    n = int(input('Enter Number of Elements: ').strip())

    a = list(map(int, input('Enter Number: ').rstrip().split()))

    result = lonelyinteger(a)

    print(f'Got Result: {result}')
