def int_to_roman(num):
    if type(num) != int or num >= 4000 or num <= 0:
        return "Please enter an integer between 1 and 3999"
    else:
        roman_num = ""
        units_digit = num % 10
        num -= units_digit
        num = int(num/10)
        tens_digit = num % 10
        num -= tens_digit
        num = int(num/10)
        hundreds_digit = num % 10
        num -= hundreds_digit
        num = int(num/10)
        thousands_digit = num
        
        roman_num = "M" * thousands_digit

        if hundreds_digit == 4:
            roman_num += "CD"
        if hundreds_digit == 9:
            roman_num += "CM"
        if hundreds_digit <= 3:
            roman_num += "C" * hundreds_digit
        if hundreds_digit >= 5 and hundreds_digit <= 8:
            roman_num += "D" + ("C" * (hundreds_digit-5))

        if tens_digit == 4:
            roman_num += "XL"
        if tens_digit == 9:
            roman_num += "XC"
        if tens_digit <= 3:
            roman_num += "X" * tens_digit
        if tens_digit >= 5 and tens_digit <= 8:
            roman_num += "L" + ("X" * (tens_digit-5))

        if units_digit == 4:
            roman_num += "IV"
        if units_digit == 9:
            roman_num += "IX"
        if units_digit <= 3:
            roman_num += "I" * units_digit
        if units_digit >= 5 and units_digit <= 8:
            roman_num += "V" + ("I" * (units_digit-5))
        return roman_num



print(int_to_roman(500))
