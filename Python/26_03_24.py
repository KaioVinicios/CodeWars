'''6 kyu "Consecutive strings" by g964
You are given an array(list) strarr of strings and an integer k. Your task is to return the first longest string consisting of k consecutive strings taken in the array.
n being the length of the string array, if n = 0 or k > n or k <= 0 return "" (return Nothing in Elm, "nothing" in Erlang).'''

def longest_consec(strarr, k):
    if len(strarr) == 0 or k > len(strarr) or k <= 0:
        return ''
    concatenate = []
    for i in range(len(strarr) - k + 1):
        concatenate.append(''.join(strarr[i:i+k]))
    return max(concatenate, key=len)
