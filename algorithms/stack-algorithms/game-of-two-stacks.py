# task: given two stacks, and an integer x, write an algorithm to compute
#       the maximum number of elements you can pop without their sum exceeding integer x

def game_of_two_stacks(l, x):
    s = 0
    count = 0
    while s <= x:
        m_i = 0
        m_v = l[0][-1]
        for i in range(1, len(l)):
            if l[i][-1] < m_v:
                m_v = l[i][-1]
                m_i = i

        s += l[m_i].pop()
        if s <= x:
            count += 1
    return count

A = [[1, 6, 4, 2, 4],
     [5, 8, 1, 2]]
print(game_of_two_stacks(A, 10))
