''' 5 kyu "Number of trailing zeros of N!" by Ivan
Write a program that will calculate the number of trailing zeros in a factorial of a given number.

Ex:
zeros(6) = 1
# 6! = 1 * 2 * 3 * 4 * 5 * 6 = 720 --> 1 trailing zero
zeros(12) = 2
# 12! = 479001600 --> 2 trailing zeros'''

def zeros(n):
    numbersOfZero = 0
    while n >= 5:
        n //= 5
        numbersOfZero += n 
    return numbersOfZero

'''def zeros(n): # Previous
    numbersOfZero = 0
    factorial = 1
    numbersInFactorial = []
    for fact in range(n + 1, 0, -1):
        factorial *= fact
    while factorial > 0:
        digit = factorial % 10
        numbersInFactorial.append(digit)
        factorial //= 10

    for number in numbersInFactorial:
        if number == 0:
            numbersOfZero += 1
        else: 
            break
    print(numbersOfZero)
    return numbersOfZero'''
