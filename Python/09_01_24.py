''' 7 kyu "Reverse words" by Jnicol
Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained. '''

def reverse_words(text):
    return ' '.join([word[::-1] for word in text.split(' ')])
