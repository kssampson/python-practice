# Complete the calculate_average function which accepts
# a list of numerical values and returns the average of
# the numbers.
#
# If the list of values is empty, the function should
# return None
#
# Pseudocode is available for you

def calculate_average(values):
    aver = 0
    num_count = 0
    for value in values:
        num_count += 1
        aver = (aver + value)
    return aver/num_count

print(calculate_average([1,2,3,4]))






#avera all
#empty none
