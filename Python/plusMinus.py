import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    positives, negatives, zeroes = 0, 0, 0

    for number in arr:
        if number == 0:
            zeroes += 1
        elif number < 0:
            negatives += 1
        else:
            positives += 1

    max_length = len(arr)

    print(f"{(positives / max_length):.6f}")
    print(f"{(negatives / max_length):.6f}")
    print(f"{(zeroes / max_length):.6f}")

if __name__ == '__main__':
    n = int(input("Enter count of number: ").strip())

    arr = list(map(int, input("Enter numbers: ").rstrip().split()))

    plusMinus(arr)
