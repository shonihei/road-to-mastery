# task: given a stack, using only one temporary stack, sort the content from largest to smallest
#       where smallest element resides at the top of the stack

def sort_stack(stack):
    if not stack:
        return stack
    temp = [stack.pop()]
    t = 0
    counter = 0
    while stack:
        t = stack.pop()
        while temp and t > temp[-1]:
            stack.append(temp.pop())
            counter += 1
        temp.append(t)
        while counter:
            temp.append(stack.pop())
            counter -= 1
    return temp

A = [10, 23, 1, 12, 5, -3]
print(A)
A = sort_stack(A)
print(A)
