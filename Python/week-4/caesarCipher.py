import string

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    # Write your code here
    alphal = string.ascii_lowercase
    alphaU = string.ascii_uppercase

    s = list(s)
    for i in range(len(s)):
        if(s[i].isalpha() and s[i].islower()):
            s[i] = alphal[(alphal.index(s[i]) + k)%len(alphal)]
        elif(s[i].isalpha() and s[i].isupper()):
            s[i] = alphaU[(alphaU.index(s[i]) + k)%len(alphaU)]
    return ''.join(s)

if __name__ == '__main__':
    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    print(f'Result: {result}')
