''' 5 kyu "Moving Zeros To The End" by xcthulhu
Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.
move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0] '''

def move_zeros(lst):
    result = []
    for num in lst:
        if num != 0:
            result.append(num)
    while len(result) < len(lst):
        result.append(0)

    return result
