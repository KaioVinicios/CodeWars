''' 6 kyu "Two Sum" by wthit56
Write a function that takes an array of numbers (integers for the tests) and a target number. It should find two different items in the array that, when added together, give the target value. The indices of these items should then be returned in a tuple / list (depending on your language) like so: (index1, index2). '''

def two_sum(numbers, target):
    for f in range(len(numbers)):
        for s in range(len(numbers)):
            if s != f and numbers[f] + numbers[s] == target:
                return (f, s)
            