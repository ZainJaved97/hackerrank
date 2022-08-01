#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    # Write your code here
    res = []
    for grade in grades:
        rem = 5 - (grade % 5)
        if grade < 35:
            res.append(grade)
        elif rem < 3:
            res.append(grade + rem)
        else:
            res.append(grade)

    return res

if __name__ == '__main__':
    grades_count = int(input().strip())

    # grades = [43, 57, 84, 39]
    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    print(f'Result: {result}')
