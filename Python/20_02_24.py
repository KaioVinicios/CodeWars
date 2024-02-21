''' 5 kyu "Regex Password Validation" by EricFreeman
You need to write regex that will validate a password to make sure it meets the following criteria:

At least six characters long
contains a lowercase letter
contains an uppercase letter
contains a digit
only contains alphanumeric characters (note that '_' is not alphanumeric)
'''
regex="^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z0-9]{6,}$"

''' ^ : Início da linha.
(?=.*[a-z]) : Lookahead positivo para garantir que a senha contenha pelo menos uma letra minúscula.
(?=.*[A-Z]) : Lookahead positivo para garantir que a senha contenha pelo menos uma letra maiúscula.
(?=.*\d) : Lookahead positivo para garantir que a senha contenha pelo menos um dígito.
[a-zA-Z0-9]{6,} : Corresponde a seis ou mais caracteres alfanuméricos.
$ : Fim da linha.'''
