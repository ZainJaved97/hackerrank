from datetime import datetime


#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#



def timeConversion(s):
    io = datetime.strptime(s, '%I:%M:%S%p')
    return str(io.time())

if __name__ == '__main__':

    # s = input()

    s = '07:05:45PM'

    result = timeConversion(s)

    print(f'Got Result: {result}')

