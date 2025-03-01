def int_to_roman(num):
    if num >= 4000:
        print("Please enter a number less than 4000")
    if num <= 0:
        print("Please enter a positive number")
    if type(num) != int:
        print("Please enter an integer")
    else:
        roman_num = ""
        units_digit = num % 10
        num -= units_digit
        tens_digit = num % 100
        num -= tens_digit
        hundreds_digit = num % 1000
        num -= hundreds_digit
        thousands_digit = num
        
        roman_num = "M" * thousands_digit

"int_to_roman(3999)"
