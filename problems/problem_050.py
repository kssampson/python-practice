# Write a function that meets these requirements.
#
# Name:       halve_the_list
# Parameters: a single list
# Returns:    two lists, each containing half of the original list
#             if the original list has an odd number of items, then
#             the extra item is in the first list
#
# Examples:
#    * input: [1, 2, 3, 4]
#      result: [1, 2], [3, 4]
#    * input: [1, 2, 3]
#      result: [1, 2], [3]

def halve_the_list(lst):
    list1 = []
    list2 = []
    for item in lst:
        if len(list1) < len(lst)/2:
            list1.append(item)
        else:
            list2.append(item)
    return list1, list2


print(halve_the_list([1, 2, 3, 4]))
