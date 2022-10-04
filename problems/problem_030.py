# Complete the find_second_largest function which accepts
# a list of numerical values and returns the second largest
# in the list
#
# If the list of values is empty, the function should
# return None
#
# If the list of values has only one value, the function
# should return None
#
# Write out some pseudocode before trying to solve the
# problem to get a good feel for how to solve it.

def find_second_largest(values):
    if values == []:
        return None
    second = 0
    largest = 0
    for value in values:
        if value > largest:
            largest = value
    for value in values:
        if value > second and value < largest:
            second = value

    return second

print(find_second_largest([1,6,7,10]))
print(find_second_largest([]))





#'1 5 6 7'
