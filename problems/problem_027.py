# Complete the max_in_list function to find the
# maximum value in a list
#
# If the list is empty, then return None.
#

def max_in_list(values):
    if values == []:
        return None
    maximum = 0
    for value in values:
        if values == []:
            return None

        if value >= maximum:
            maximum = value
    return maximum

print(max_in_list([1, 18, 9, 5]))
print(max_in_list([]))
