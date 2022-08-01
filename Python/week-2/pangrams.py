import string
#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def pangrams(s):
    # Write your code here
    alphabets = list(string.ascii_lowercase)
    s = s.lower()

    for alphabet in alphabets:
        if alphabet not in s:
            return 'not pangram'

    return 'pangram'

if __name__ == '__main__':
    s = input()
    
    # s = 'We promptly judged antique ivory buckles for the prize'

    result = pangrams(s)

    print(f'Got Result: {result}')
