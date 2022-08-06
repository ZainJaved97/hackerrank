#
# Complete the 'separateNumbers' function below.
#
# The function accepts STRING s as parameter.
#

def separateNumbers(s):
    # Write your code here
    count = len(s)

    for l in range(1, count):
        first = int(s[0:0+l])
        start = first
        combined = ''
        while len(combined) < count:
            
            combined += str(first)
            first += 1
        
        if combined == s:
            print(f'YES {start}')
            return 

    print('NO')


if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        separateNumbers(s)
