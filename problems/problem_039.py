# Complete the reverse_dictionary function which has a
# single parameter that is a dictionary. Return a new
# dictionary that has the original dictionary's values
# for its keys, and the original dictionary's keys for
# its values.
#
# Examples:
#   * input:  {}
#     output: {}
#   * input:  {"key": "value"}
#     output: {"value", "key"}
#   * input:  {"one": 1, "two": 2, "three": 3}
#     output: {1: "one", 2: "two", 3: "three"}




input = {"Cats": "Toe beans", "Potatoes": "Po-tat-toe", "Tow-truck":"Hey where's my car?"}

def reverse_dictionary(dictionary):
    new_dictionary = {}
    for key in dictionary:
        new_key = dictionary[key]
        new_dictionary[new_key] = key
    return new_dictionary



        # "key" = dictionary [value]
        # "value" = dictionary [key]
    return dictionary
print(reverse_dictionary(input))










#     input:  {}
#     output: {}
#   * input:  {"key": "value"}
#     output: {"value", "key"}
#   * input:  {"one": 1, "two": 2, "three": 3}
#     output: {1: "one", 2: "two", 3: "three"}
