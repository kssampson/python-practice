# Write a function that meets these requirements.
#
# Name:       shift_letters
# Parameters: a string containing a single word
# Returns:    a new string with all letters replaced
#             by the next letter in the alphabet
#
# If the letter "Z" or "z" appear in the string, then
# they would get replaced by "A" or "a", respectively.
#
# Examples:
#     * inputs:  "import"
#       result:  "jnqpsu"
#     * inputs:  "ABBA"
#       result:  "BCCB"
#     * inputs:  "Kala"
#       result:  "Lbmb"
#     * inputs:  "zap"
#       result:  "abq"
#
# You may want to look at the built-in Python functions
# "ord" and "chr" for this problem

def shift_letters(word):
    new_word = ''
    for letter in word:
        if letter == 'z':
            new_word += 'a'
        elif letter == 'Z':
            new_word += 'A'
        else:
            new_ord = ord(letter) + 1
            new_chr = chr(new_ord)
            new_word = new_word + new_chr
    return new_word
print(shift_letters("zpoop"))
