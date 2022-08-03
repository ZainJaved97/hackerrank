#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

from math import floor


def isBalanced(s):
    # Write your code here

    if len(s) % 2 != 0 or s[0] in [')', '}', ']']:
        return 'NO'

    stack = []
    for c in s:
        if c in ['(', '{', '[']:
            stack.append(c)
        else:
            if len(stack) and stack[-1] == '(' and c == ')':
                stack.pop()
            elif len(stack) and stack[-1] == '{' and c == '}':
                stack.pop()
            elif len(stack) and stack[-1] == '[' and c == ']':
                stack.pop()
            else:
                return 'NO'

    return 'YES' if len(stack) == 0 else 'NO'

if __name__ == '__main__':
    for pair in ['{[()]}', '{[(])}', '{{[[(())]]}}', '{{)[](}}', '{(([])[])[]]}']:
        result = isBalanced(pair)

        print(f'Result: {result}')
