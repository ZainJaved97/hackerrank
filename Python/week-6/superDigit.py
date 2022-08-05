#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

def superDigit(n, k):
    # Write your code here
    def total(n: str) -> int:
        return sum([int(i) for i in n])
    
    def findSingleDigit(n: int) -> int:
        if n <= 9:
            return n
        return findSingleDigit(total(str(n)))
    
    return findSingleDigit(total(n) * k)

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    print(f'Result: {result}')
