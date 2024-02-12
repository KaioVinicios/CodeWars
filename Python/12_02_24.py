
'''' 6 kyu "Break camelCase" by Hakt
Complete the solution so that the function will break up camel casing, using a space between words.
camelCasing_ex = 'helloWorld' -> "hello World"
'''

def solution(s):
    result = ''
    for w in s:
        if w.isupper():
            result += ' '
        result += w
    return result
