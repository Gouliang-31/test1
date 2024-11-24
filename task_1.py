def roman_to_arabic(roman):
    roman_to_int = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    arabic_number = 0
    prev_value = 0

    for char in reversed(roman):
        value = roman_to_int[char]
        if value < prev_value:
            arabic_number -= value
        else:
            arabic_number += value
        prev_value = value

    return arabic_number

roman_number = "MCMXCIV"  # 1994
arabic_number = roman_to_arabic(roman_number)
print(f"Римское число {roman_number} = Арабское число {arabic_number}")