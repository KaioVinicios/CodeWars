'''5 kyu "Scramblies" by Joh_pot
Complete the function scramble(str1, str2) that returns true if a portion of str1 characters can be rearranged to match str2, otherwise returns false.
Ex: scramble('cedewaraaossoqqyt', 'codewars') ==> True'''

def scramble(s1, s2):
    dic_s1 = {}
    dic_s2 = {}
    for l in s1:
        dic_s1[l] = dic_s1.get(l, 0) + 1
    for l in s2:
        dic_s2[l] = dic_s2.get(l, 0) + 1
    for l, c in dic_s2.items():
        if c > dic_s1.get(l, 0):
            return False
    return True
