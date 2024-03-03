def is_merge(s='', part1='', part2=''):
    alphabet_s = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
    alphabet_parts = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
    
    teste_lista = []
    for letra in s:
        teste_lista.append(letra)
    
    if part1 not in teste_lista[0:len(part1)]:
        if part2 not in teste_lista[0:len(part2)]:
            return False

     
    part1 += part2
    s.lower()
    part1.lower()

    for letra in s:
        if letra in alphabet_s.keys():
            alphabet_s[letra] += 1
            
    for letra in part1:
        if letra in alphabet_parts.keys():
            alphabet_parts[letra] += 1
            
    print(alphabet_s, alphabet_parts, s, part1, part2)
    
    if part1 == s:
        return True
    elif alphabet_s == alphabet_parts:
        return True
    else:
        return False
        