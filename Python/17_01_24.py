'''6 kyu "Stop gninnipS My sdroW!" by xDranik
Write a function that takes in a string of one or more words, and returns the same string, but with all words that have five or more letters reversed (Just like the name of this Kata). Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present.'''

def spin_words(sentence):
    result = ''
    sentence = sentence.split(' ')
    for word in range(0, len(sentence)):
        if len(sentence[word]) >= 5:
            result += sentence[word][::-1]
        else:
            result += sentence[word]
        
        if len(sentence) > 1 and word != len(sentence) - 1:
                result += ' ' 
    return result
