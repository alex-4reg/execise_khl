"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.

Additionally, if the number is negative, return 0.

Note: If the number is a multiple of both 3 and 5, only count it once.
"""
import time


def main():
    number_to_count = 100_000_000
    start_time1 = time.perf_counter()
    print(get_sum_of_multiples(number_to_count, 3, 5))
    finish_time1 = time.perf_counter()
    execution_time1 = finish_time1 - start_time1

    start_time2 = time.perf_counter()
    print(calculate_sum_linearly(number_to_count))
    finish_time2 = time.perf_counter()
    execution_time2 = finish_time2 - start_time2
    print(f"On calculating {number_to_count:_} elements 1-st method is faster than 2-nd by "
          f"{((execution_time2 / execution_time1) - 1) * 100:.1f} % ({execution_time1:.5f} sec vs "
          f"{execution_time2:.5f} sec).")


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


def calculate_sum_linearly(number):
    sum_of_multiples = 0
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            sum_of_multiples += i

    return sum_of_multiples


if __name__ == "__main__":
    main()
