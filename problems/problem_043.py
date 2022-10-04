# Complete the find_indexes function which accepts two
# parameters, a list and a search term. It returns a new
# list that contains the indexes of the search term in
# the search list.
#
# Remember that indexes in Python are zero-based. That
# means the first element in the list is index 0.
#
# Examples:
#   * search_list:  [1, 2, 3, 4, 5]
#     search_term:  4
#     result:       [3]
#   * search_list:  [1, 2, 3, 4, 5]
#     search_term:  6
#     result:       []
#   * search_list:  [1, 2, 1, 2, 1]
#     search_term:  1
#     result:       [0, 2, 4]
#
# Look up the enumerate function to help you with this problem.

 def find_indexes(search_list, search_term):
     new_index = []
     for spot1, spot2 in enumerate(search_list):
         if value == search_term:
            new_index.append(spot1)
    return new_index


#print(enumerate([1,2,3,4]))
# def counted(list):
#     for count, value in enumerate(list):
#       return(counted(list))
# print(counted([1,2,3,4]))
