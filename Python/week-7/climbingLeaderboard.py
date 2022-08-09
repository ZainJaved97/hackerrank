#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#

def climbingLeaderboard(ranked, player):
    # Write your code here
    result = []
    ranked = sorted(list(set(ranked)), reverse=True)
    
    def binary_search(data, score):
        # note the binary search here is dealing
        # the reversed sorted array
        low = 0
        upper = len(data) - 1
        
        while low <= upper:
            mid = low + (upper - low) // 2
            if data[mid] > score:
                low = mid + 1
            elif data[mid] < score:
                upper = mid - 1
            else:
                return mid
        # insert the score if not found
        insertPosition = low + (upper - low) // 2 + 1
        ranked.insert(insertPosition, score)
        return binary_search(ranked, score)
    
    def insert_score_and_get_rank(score):
        # only insert the unique value to the list
        # the head insertion
        if score > ranked[0]:
            ranked.insert(0, score)
            return 1
        
        # the tail insertion
        if score < ranked[len(ranked) - 1]:
            ranked.insert(len(ranked), score)
            return len(ranked) - 1 + 1
        
        # perform binary search to lower down the search time
        # since the ranked array is uniquely ordered
        # insert the not found score and recursively perform binary search
        return binary_search(ranked, score) + 1
        
    for score in player:
        rank = insert_score_and_get_rank(score)
        result.append(rank)
        
    return result

if __name__ == '__main__':
    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    print(f'Result: {result}')

