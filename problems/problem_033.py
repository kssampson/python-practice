# Complete the sum_of_first_n_even_numbers function which
# accepts a numerical count n and returns the sum of the
# first n even numbers
#
# If the value of the limit is less than 0, then it should
# return None
#
# Examples:
#   * -1 returns None
#   * 0 returns 0
#   * 1 returns 0+2=2
#   * 2 returns 0+2+4=6
#   * 5 returns 0+2+4+6+8+10=30
#
# Write out some pseudocode before trying to solve the
# problem to get a good feel for how to solve it.






# #def sum_of_first_n_even_numbers(limit):
#     #sum = 0
#     #limit = range(limit + 1)
#     #for number in limit:
#         #if number %2 == 0:
#             #sum = sum + number
#     return sum
# #print(sum_of_first_n_even_numbers(5))


def sum_of_first_n_numbers(limit):
    sum = 0
    limit = range(limit + 1)
    for number in limit:
        sum = sum + number
    return sum*2
print(sum_of_first_n_numbers(5))
