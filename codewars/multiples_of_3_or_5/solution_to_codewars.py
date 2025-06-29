def solution(number):
    return get_sum_of_multiples(number, 3, 5)


def get_sum_of_multiples(number: int, *dividers):
    if number < 0:
        return 0

    sum_of_multiples = list()
    for divider in dividers:
        sum_of_multiples.extend(fill_list_of_divisible_numbers(number, divider))

    return sum(set(sum_of_multiples))


def fill_list_of_divisible_numbers(number: int, divider):
    return list(range(divider, number - get_remainder(number, divider) + 1, divider))


def get_remainder(number: int, divider: int):
    return (number - 1) % divider
