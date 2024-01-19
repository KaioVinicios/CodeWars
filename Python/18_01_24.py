''' 7 kyu "Vowel Count" by Jayeshcp
Return the number (count) of vowels in the given string.
We will consider a, e, i, o, u as vowels for this Kata (but not y).
The input string will only consist of lower case letters and/or spaces.'''

def get_count(sentence):
    sentence = sentence.strip()
    vocals = ['a', 'e', 'i', 'o','u']
    cont = 0
    for l in range(0, len(sentence)):
        if sentence[l] in vocals:
            cont += 1
    return cont