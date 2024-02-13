''''6 kyu "Find the odd int" by Rbuclkey
Given an array of integers, find the one that appears an odd number of times.
There will always be only one integer that appears an odd number of times.'''

def find_it(seq):
    numbers = []
    for n in seq:
        if n not in numbers:
            numbers.append([n, 0])
    for i in numbers:
        for n in seq:
            if n == i[0]:
                i[1] += 1
        if i[1] % 2 != 0:
            return i[0]
            