#
# Complete the 'closestNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def closestNumbers(arr):
    # Write your code here
    arr = sorted(arr)
    mapping = {}
		
    for i in range(len(arr) - 1):
        diff = abs(arr[i] - arr[i + 1])
				
        if diff not in mapping:
            mapping[diff] = [arr[i], arr[i + 1]]
            continue

        mapping[diff] += [arr[i], arr[i + 1]]
    
    minimum = min(mapping.keys())

    return mapping[minimum]


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = closestNumbers(arr)

    print(f'Result: {result}')
