''' 6 kyu "Valid Braces" by xDranik
Write a function that takes a string of braces, and determines if the order of the braces is valid. It should return true if the string is valid, and false if it's invalid.
All input strings will be nonempty, and will only consist of parentheses, brackets and curly braces: ()[]{}.
What is considered Valid?
A string of braces is considered valid if all braces are matched with the correct brace.
Examples
"(){}[]"   =>  True
"[({})](]" =>  False '''

def valid_braces(string):
    stack = []
    opening_braces = '([{'
    closing_braces = ')]}'
    brace_pairs = {')': '(', ']': '[', '}': '{'}
    
    for char in string:
        if char in opening_braces:
            stack.append(char)
        elif char in closing_braces:
            if not stack or stack.pop() != brace_pairs[char]:
                return False
    
    return len(stack) == 0
