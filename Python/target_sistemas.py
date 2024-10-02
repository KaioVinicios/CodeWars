import math

# 01
def is_perfect_square(x):
    s = int(math.sqrt(x))
    return s * s == x

def is_fibonacci():
    n = int(input("Digite um número: "))
    if is_perfect_square(5 * n * n + 4) or is_perfect_square(5 * n * n - 4):
        print(f"{n} pertence à sequência de Fibonacci.")    
    else:
        print(f"{n} não pertence à sequência de Fibonacci.")

# is_fibonacci()

# 02
def owns_a(phrase):
    phrase = phrase.lower()
    n = 0
    for letter in phrase:
        if letter == 'a':
            n += 1
    if n == 0:
        print("Não há letras 'A/a'.")
    elif n >= 1:
        print(f"A string possui {n} letras 'A/a'.")

owns_a("AtesTea")

# 03
indice = 12 
soma = 0
k = 1
while k < indice:
    k += 1
    soma += k
print(soma) # 77

'''
04
a) 9
b) 128
c) 49
d) 100
e) 13
f) 20
'''

'''
05
Ligue o primeiro interruptor e deixe-o ligado por alguns minutos.
Desligue o primeiro interruptor e ligue o segundo.
Vá até a sala das lâmpadas. A lâmpada que está acesa corresponde ao segundo interruptor. A lâmpada que está quente, mas apagada, corresponde ao primeiro interruptor. A lâmpada fria e apagada corresponde ao terceiro interruptor.
'''