# Complete the gear_for_day function which returns a list of
# gear needed for the day given certain criteria.
#   * If the day is not sunny and it is a workday, the list
#     needs to contain "umbrella"
#   * If it is a workday, the list needs to contain "laptop"
#   * If it is not a workday, the list needs to contain
#     "surfboard"

def gear_for_day(is_workday, is_sunny):
    gear = []
    if is_workday:
        gear.append("laptop")
    else:
        gear.append("surfboard")
    if is_sunny:
        return gear
    else:
        gear.append("umbrella")
    return gear

print(gear_for_day(True, True))
print(gear_for_day(False, False))


#sunny + work  > umbrella
#work > laptop
#not work > surfboard
