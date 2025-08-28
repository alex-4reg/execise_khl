# Given the string representations of two integers, return the string representation of the sum of those integers.
#
# For example:
# sumStrings('1','2') // => '3'
# A string representation of an integer will contain no characters besides the ten numerals "0" to "9".
# I have removed the use of BigInteger and BigDecimal in java
# Python: your solution need to work with huge numbers (about a million digits), converting to int will not work.


def convert_str_to_int(string_digit):
    result = [ord(x) - 48 for x in string_digit]

    number = 0

    for index in range(len(result)):
        number += result[index] * pow(10, len(result) - index - 1)

    return number


def sumStrings(number1, number2):
    return str(convert_str_to_int(number1) + convert_str_to_int(number2))


print(sumStrings("333", "10000"))  # 10333
