def validRomanNumber(s):
    import re
    thousand = 'M{0,3}'
    hundred = '(C[MD]|D?C{0,3})'
    ten = '(X[CL]|L?X{0,3})'
    digit = '(I[VX]|V?I{0,3})'
    return bool(re.match(thousand + hundred + ten + digit + '$', s))


if __name__ == '__main__':
    inputs = [
        'III',
        'IV',
        'LVIII',
        'MCMXCIV',
        'MMMMCL',
        'LLCIX'
    ]

    for inp in inputs:
        print validRomanNumber(inp)
