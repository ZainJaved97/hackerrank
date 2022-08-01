
#
# Complete the 'matchingStrings' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY strings
#  2. STRING_ARRAY queries
#

def matchingStrings(strings, queries):
    # Write your code here
    res = [0] * len(queries)

    for idx, query in enumerate(queries):
        res[idx] = strings.count(query)

    return res

if __name__ == '__main__':
    # strings_count = int(input().strip())

    # strings = []

    # for _ in range(strings_count):
    #     strings_item = input()
    #     strings.append(strings_item)

    # queries_count = int(input().strip())

    # queries = []

    # for _ in range(queries_count):
    #     queries_item = input()
    #     queries.append(queries_item)

    strings = [
        'def',
        'de',
        'fgh',
    ]

    queries = [
        'de',
        'lmn',
        'fgh',
    ]

    res = matchingStrings(strings, queries)
    print(f'Got Result: {res}')
