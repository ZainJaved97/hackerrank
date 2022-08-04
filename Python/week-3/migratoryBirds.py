
#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    # Write your code here

    unique_elems = set(arr)
    map = {elem: arr.count(elem) for elem in unique_elems}
    return max(map, key=map.get)

if __name__ == '__main__':
    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    print(f'Result: {result}')
