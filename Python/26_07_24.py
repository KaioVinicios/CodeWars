''' 6 kyu "Sort the odd" by fyvfyv
You will be given an array of numbers. You have to sort the odd numbers in ascending order while leaving the even numbers at their original positions.

Examples
[7, 1]  =>  [1, 7]
[5, 8, 6, 3, 4]  =>  [3, 8, 6, 5, 4]
[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  =>  [1, 8, 3, 6, 5, 4, 7, 2, 9, 0] '''

def sort_array(source_array):
    odd_numbers = []
    odd_positions = []
    for c in range(len(source_array)):
        if source_array[c] % 2 != 0:
            odd_numbers.append(source_array[c])
            odd_positions.append(c)
    odd_numbers.sort()
    for c in range(len(source_array)):
        if c in odd_positions:
            source_array[c] = odd_numbers[0]
            del odd_numbers[0]
    return source_array
