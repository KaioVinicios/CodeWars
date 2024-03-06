''' 6 kyu Sum of Digits / Digital Root by user578387

Digital root is the recursive sum of all the digits in a number.
Given n, take the sum of the digits of n. If that value has more than one digit, continue reducing in this way until a single-digit number is produced. The input will be a non-negative integer.

Ex: 132189  -->  1 + 3 + 2 + 1 + 8 + 9 = 24  -->  2 + 4 = 6'''

def digital_root(n):
    while n > 9:
        n = sum(int(digit) for digit in str(n))
    return n

'''def digital_root(n): Previous
    result = n
    isolated_numbers = []
    
    while result > 9:
        n = str(result)
        result = 0
        for number in n:
            isolated_numbers.append(int(number))
        result = sum(isolated_numbers)
    return result'''
        