''' 8 kyu 'Basic Mathematical Operations' by Quickz
The function should take three arguments - operation(string/char), value1(number), value2(number).
The function should return result of numbers after applying the chosen operation.
'''

def basic_op(operator, value1, value2):
    #your code here
    if operator == '+':
        return (value1 + value2)
    elif operator == '-':
        return (value1 - value2)
    elif operator == '*':
        return (value1 * value2)
    elif operator == '/':
        return(value1 / value2)
    else:
        return ('Operator does not exist.')
