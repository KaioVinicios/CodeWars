''' 6 kyu "Find the unique number" by Isqua
There is an array with some numbers. All numbers are equal except for one. Try to find it!
find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55
Its guaranteed that array contains at least 3 numbers.
The tests contain some very huge arrays, so think about performance. '''

def find_uniq(arr): 
    first_num = arr[0]
    if first_num != arr[1] and first_num != arr[2]:
        return first_num
    for n in arr[1::]:
        if n != first_num:
            return n
        