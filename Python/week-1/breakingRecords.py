#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    most_min, most_max = scores[0], scores[0]
    min_count, max_count = 0, 0

    for score in scores[1:]:
        if score < most_min:
            most_min = score
            min_count += 1
        
        elif score > most_max:
            most_max = score
            max_count += 1

    return [max_count, min_count]

if __name__ == '__main__':
    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)
    output = ' '.join(map(str, result))

    print(f"Output: {output}")
