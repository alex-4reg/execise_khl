# Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.
#
# move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]

def move_zeros(list_numbers):
    non_zeros_list = [x for x in list_numbers if x != 0]
    zeros_list = [x for x in list_numbers if x == 0]
    return non_zeros_list + zeros_list


print(move_zeros([1, 0, 1, 2, 0, 1, 3]))