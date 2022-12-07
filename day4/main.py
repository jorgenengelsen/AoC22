import re

def find_complete_overlap(left_range, right_range):
    left_in_right = True
    right_in_left = True


    if len(left_range) == 0:
        if not left_range.start in right_range:
            left_in_right = False

    for section in left_range:
        if section not in right_range:
            left_in_right = False
    
    if len(right_range) == 0:
        if not right_range.start in left_range:
            right_in_left = False


    for section in right_range:
        if section not in left_range:
            right_in_left = False

    if left_in_right or right_in_left:
        return True
    else:
        return False

def find_partial_overlap(left_range, right_range):
    left_in_right = False
    right_in_left = False


    if len(left_range) == 0:
        if left_range.start in right_range:
            left_in_right = True

    for section in left_range:
        if section in right_range:
            left_in_right = True
    
    if len(right_range) == 0:
        if right_range.start in left_range:
            right_in_left = True


    for section in right_range:
        if section in left_range:
            right_in_left = True

    if left_in_right or right_in_left:
        return True
    else:
        return False



with open("day3/input.txt") as f:
    pairs = f.readlines()

complete_overlapping_pairs = 0
partial_overlapping_pairs = 0

for pair in pairs:
    range_limits = re.match("(\d*)-(\d*),(\d*)-(\d*)", pair)

    range_limits = range_limits.groups()

    range_limits = [int(range_limit) for range_limit in range_limits]

    left_range = range(range_limits[0], range_limits[1]+1)
    right_range = range(range_limits[2], range_limits[3]+1)

    complete_overlapping_pairs += find_complete_overlap(left_range, right_range)
    partial_overlapping_pairs += find_partial_overlap(left_range, right_range)
    


print(complete_overlapping_pairs)
print(partial_overlapping_pairs)