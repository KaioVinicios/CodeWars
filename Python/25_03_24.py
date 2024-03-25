''' 5 kyu "Simple Pig Latin" by user2505876
Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

Examples
pig_it('Hello world !')     # elloHay orldway ! '''

def pig_it(text):
    words_list = text.split()
    for word in range(len(words_list)):
        reversed_word = ''
        if words_list[word].isalpha(): 
            reversed_word = words_list[word][1::]    
            reversed_word += words_list[word][0] + "ay"
            words_list[word] = reversed_word
    return ' '.join(words_list)
        