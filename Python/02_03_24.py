# https://www.codewars.com/kata/52f787eb172a8b4ae1000a34/train/python

def zeros(n):
    numbersOfZero = 0
    factorial = 1
    numbersInFactorial = []
    for fact in range(n + 1 , 0, -1):
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
    return numbersOfZero
