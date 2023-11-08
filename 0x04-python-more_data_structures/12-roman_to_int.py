def roman_to_int(roman_string):
    if not roman_string or not isinstance(roman_string, str):
        return 0
    number = 0
    i = 0
    while i < len(roman_string):
        if i < len(roman_string) - 1 and roman_string[i:i+2] in ["IV",
                                                                 "IX",
                                                                 "XC",
                                                                 "CD",
                                                                 "CM"]:
            number += roman_helper(roman_string[i+1]) - \
                roman_helper(roman_string[i])
            i += 2
        else:
            number += roman_helper(roman_string[i])
            i += 1
    return number


def roman_helper(letter):
    doc = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    for key, value in doc.items():
        if key == letter:
            return value
    return 0
