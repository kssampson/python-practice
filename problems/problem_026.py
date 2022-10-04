# Complete the calculate_grade function which accepts
# a list of numerical scores each between 0 and 100.
#
# Based on the average of the scores, the function
# returns
#   * An "A" for an average greater than or equal to 90
#   * A "B" for an average greater than or equal to 80
#     and less than 90
#   * A "C" for an average greater than or equal to 70
#     and less than 80
#   * A "D" for an average greater than or equal to 60
#     and less than 70
#   * An "F" for any other average

def calculate_grade(values):
    grades = []
    for value in values:
        if value >= 90:
            grades.append("A")
    
        elif value >= 80:
            grades.append("B")
           
        elif value >= 70:
            grades.append("C")
           
        elif value >= 60:
            grades.append("D")
          
        else:
            grades.append("F")
    return grades

print(calculate_grade([99, 88, 66, 79, 80]))