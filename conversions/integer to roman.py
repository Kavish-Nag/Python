while True:
    def int_to_roman(num):
        roman_numerals = {1000: 'M', 900: 'CM', 500: 'D',  400: 'CD',  100: 'C', 90: 'XC',50: 'L',40: 'XL',10: 'X',9: 'IX',5: 'V',4: 'IV',1: 'I'}
        result = ""
        for value in sorted(roman_numerals.keys(), reverse=True):
                while num >= value:
                    result += roman_numerals[value]
                    num -= value
        return result
    number = int(input("Enter number:"))
    if number == 0:
        print("Not Applicable")
    elif number < 0:
        roman_numeral = int_to_roman(abs(number))
        print(f"The Roman numeral for {number} is not applicable. However, the Roman numeral for its absolute value is: {roman_numeral}")
    else:
        roman_numeral = int_to_roman(number)
        print(f"The Roman numeral for {number} is: {roman_numeral}")
