'''7 kyu 'Shortest Word' by PG1
Simple, given a string of words, return the length of the shortest word(s).
String will never be empty and you do not need to account for different data types.'''

def find_short(s):
    word = ''
    words = []
    for n in range(0, len(s), 1):
        if s[n] != ' ' :
            word += s[n]
        else:
            words.append(len(word))
            word = ''
    words.append(len(word))
    return min(words)