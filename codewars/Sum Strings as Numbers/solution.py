# Given the string representations of two integers, return the string representation of the sum of those integers.
#
# For example:
# sumStrings('1','2') // => '3'
# A string representation of an integer will contain no characters besides the ten numerals "0" to "9".
# I have removed the use of BigInteger and BigDecimal in java
# Python: your solution need to work with huge numbers (about a million digits), converting to int will not work.

chars = [x for x in range(48, 58)]
print(chars)
print(chr(ord('1')))


def check_is_digits_only(string_digit):
    converted_to_int = [x for x in string_digit if ord(x) in chars]
    print(converted_to_int)
    return len(string_digit) == len(converted_to_int)

def convert_str_to_int(string_digit):

    sign = 1


    result = [ord(x) - 48 for x in string_digit]
    print(result)

    if string_digit[0] == '-':
        sign = -1
        del result[0]
        print("-")

    print(result)


    number = 0

    for index in range(len(result)):
        number += result[index] * pow(10, len(result) - index - 1)

    print(number * sign)
    return number * sign


print(check_is_digits_only('1956565656565656565'))
convert_str_to_int('-2362')

def sumStrings(number1, number2):
    return str(convert_str_to_int(number1) + convert_str_to_int(number2))

print(sumStrings("10", "102"))