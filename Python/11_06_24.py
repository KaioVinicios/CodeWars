''' 6 kyu "Give me a Diamond" by Jayeshcp
You need to return a string that looks like a diamond shape when printed on the screen, using asterisk (*) characters. Trailing spaces should be removed, and every line must be terminated with a newline character (\n).

Return null/nil/None/... if the input is an even number or negative, as it is not possible to print a diamond of even or negative size.

Examples
A size 3 diamond:

 *
***
 *
...which would appear as a string of " *\n***\n *\n" '''

def diamond(n):
    if n % 2 == 0 or n <= 0:
        return None
    else:
        midle = (n // 2) + 1
        result = ''
        quant = 1
        for line in range(1, n + 1):
            if line > midle:
                quant -= 2
            if line == 1:
                spaces = midle - 1
            else:
                if line <= midle:
                    spaces = midle - line
                else:
                    spaces = line - midle
            result += ' ' * spaces + '*' * quant + '\n'
            if line < midle:
                quant += 2
        return result
