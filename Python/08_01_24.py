''''7 kyu "Disemvowel Trolls" by oushii
Your task is to write a function that takes a string and return a new string with all vowels removed.'''

def disemvowel(string_):
    result = ''
    for w in string_ :
        if w not in 'aeiouAEIOU':
            result += w
    return result 

'''
def disemvowel(string_):
    return ''.join([w for w in string_ if w not in 'aeiouAEIOU'])
'''