# Complete the check_password function that accepts a
# single parameter, the password to check.
#
# A password is valid if it meets all of these criteria
#   * It must have at least one lowercase letter (a-z)
#   * It must have at least one uppercase letter (A-Z)
#   * It must have at least one digit (0-9)
#   * It must have at least one special character $, !, or @
#   * It must have six or more characters in it
#   * It must have twelve or fewer characters in it
#
# The string object has some methods that you may want to use,
# like ".isalpha", ".isdigit", ".isupper", and ".islower"

def check_password(password):
    for character in password:
        if (len(password) <= 12 and len(password) >= 6):
            if character.isalpha():
                if character.isdigit():
                    if character.isupper():
                        if character.islower():
                            if
            return True

         return check_password
    print(check_password(hertzBoy002!))
