''' 6 kyu "Split Strings" by jhoffner
Complete the solution so that it splits the string into pairs of two characters. If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').

Examples:
* 'abc' =>  ['ab', 'c_']
* 'abcdef' => ['ab', 'cd', 'ef'] '''

def solution(s):
    result = []
    if len(s) % 2 != 0:
        s += "_"
    for letter in range(0, len(s), 2):
        print(letter)
        result.append(s[letter:letter+2])
    return(result)
