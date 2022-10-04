# Complete the remove_duplicate_letters that takes a string
# parameter "s" and returns a string with all of the
# duplicates removed.
#
# Examples:
#   * For "abc", the result is "abc"
#   * For "abcabc", the result is "abc"
#   * For "abccba", the result is "abc"
#   * For "abccbad", the result is "abcd"
#
# If the list is empty, then return the empty string.

def remove_duplicate_letters(s):
   dupes = ""
   for letter in s:
        if letter not in dupes:
             dupes += letter

   return dupes
print(remove_duplicate_letters("yassss"))
