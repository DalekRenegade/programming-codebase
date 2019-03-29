from Valid_Roman_Number import validRomanNumber


def romanToInt(s):
    if not validRomanNumber(s):
        return -1
    roman_to_arabic = {'O': 0, 'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = temp = 0
    s = s + "O"

    for idx, c in enumerate(s[:-1]):
        if roman_to_arabic[c] < roman_to_arabic[s[idx + 1]]:
            temp = roman_to_arabic[c]
        elif temp:
            result += roman_to_arabic[c] - temp
            temp = 0
        else:
            result += roman_to_arabic[c]
    return result


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
        print inp, '=', romanToInt(inp)
