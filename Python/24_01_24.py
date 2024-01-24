'''6 kyu "Your order, please" by Iamstone
Your task is to sort a given string. Each word in the string will contain a single number. This number is the position the word should have in the result.
Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).
If the input string is empty, return an empty string. The words in the input String will only contain valid consecutive numbers.'''

def order(sentence):
    sentence = sentence.split()
    result = []
    cont = len(sentence)
    while cont > 0:
        for s in sentence:
            if str(cont) in s:
                result.insert(0, s)
        cont -= 1
    return ' '.join(result)