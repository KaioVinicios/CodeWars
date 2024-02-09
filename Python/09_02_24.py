'''5 kyu "The Hashtag Generator" by AKJYO

Here's the deal:
It must start with a hashtag (#).
All words must have their first letter capitalized.
If the final result is longer than 140 chars it must return false.
If the input or the result is an empty string it must return false.'''

def generate_hashtag(s):
    result = '#'
    s = s.split()
    for w in s:
        result += w.capitalize()
    if len(result) > 140:
        return False
    elif result[1:] == '':
        return False
    else:
        return result