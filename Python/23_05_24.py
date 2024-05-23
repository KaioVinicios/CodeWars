''' 4 kyu "Snail" by stevenbarragan
Given an n x n array, return the array elements arranged from outermost elements to the middle element, traveling clockwise.
array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
snail(array) #=> [1,2,3,6,9,8,7,4,5]

For better understanding, please follow the numbers of the next array consecutively:
array = [[1,2,3],
         [8,9,4],
         [7,6,5]]
snail(array) #=> [1,2,3,4,5,6,7,8,9] '''

def snail(snail_map):
    result = []

    if not snail_map:
        return result

    top = 0
    botton = len(snail_map) - 1
    left = 0 
    right = len(snail_map[0]) - 1

    while top <= botton and left <= right:
        for i in range(left, right + 1):
            result.append(snail_map[top][i])
        top += 1
        for i in range(top, botton + 1):
            result.append(snail_map[i][right])
        right -= 1

        if top <= botton:
            for i in range(right, left - 1, -1):
                result.append(snail_map[botton][i])
            botton -= 1
        if left <= right:
            for i in range(botton, top - 1, -1):
                result.append(snail_map[i][left])
            left += 1
    
    return result
