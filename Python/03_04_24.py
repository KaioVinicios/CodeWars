''' 6 kyu "Convert string to camel case" by Jhoffner

Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case). The next words should be always capitalized. '''


def to_camel_case(text):
    text_ = []
    letter = 0
    while letter != len(text):
        if text[letter].isalpha():
            text_.append(text[letter])
        else:
            text_.append(text[letter + 1].upper())
            letter += 1
        letter += 1 

    return ''.join(text_)
