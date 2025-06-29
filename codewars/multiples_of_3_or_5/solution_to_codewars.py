"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.

Additionally, if the number is negative, return 0.

Note: If the number is a multiple of both 3 and 5, only count it once.
"""


def solution(number):
    return get_sum_of_multiples(number, 3, 5)


def get_sum_of_multiples(number, *dividers):
    if number < 0:
        return 0

    sum_of_multiples = list()
    for divider in dividers:
        sum_of_multiples.extend(fill_list_of_divisible_numbers(number, divider))

    return sum(set(sum_of_multiples))


def fill_list_of_divisible_numbers(number, divider):
    return list(range(divider, number - get_remainder(number, divider) + 1, divider))


def get_remainder(number, divider):
    return (number - 1) % divider
