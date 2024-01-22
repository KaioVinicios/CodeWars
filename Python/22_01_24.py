''' 7 kyu "Two to One" by g964
Take 2 strings s1 and s2 including only letters from a to z. Return a new sorted string, the longest possible, containing distinct letters - each taken only once - coming from s1 or s2.'''

def longest(a1, a2):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    a = a1 + a2
    r = ''
    for l in range(0, len(alphabet)):
        if alphabet[l] in a:
            r += alphabet[l]
    return r