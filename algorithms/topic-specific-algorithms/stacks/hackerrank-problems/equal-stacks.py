# Problem : https://www.hackerrank.com/challenges/equal-stacks

# n1,n2,n3 = input().strip().split(' ')
# n1,n2,n3 = [int(n1),int(n2),int(n3)]
# h1 = [int(h1_temp) for h1_temp in input().strip().split(' ')]
# h2 = [int(h2_temp) for h2_temp in input().strip().split(' ')]
# h3 = [int(h3_temp) for h3_temp in input().strip().split(' ')]

h1 = [1, 1, 1, 2, 3]
h2 = [2, 3, 4]
h3 = [1, 4, 1, 1, 1]

def find_equal_height(h1, h2, h3):
    min_height = min(sum(h1), min(sum(h2), sum(h3)))
    
