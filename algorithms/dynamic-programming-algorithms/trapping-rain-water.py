# task: given a list of integers that represent a hight, write an algorithm
#       to find the largest area above the histogram
#
# e.g
#
#     ___             ___
#    |   |           |   |
#    |   |    ___    |   |
#    |   |___|   |___|   |
#____|     1   2   3     |__
#
# output => 3 + 2 + 3 = 8

def max_water(lst):
    max_height = lst[0]
    accum = 0

    for height in lst:
        
