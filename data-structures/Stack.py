class Stack:
    def __init__(self):
        self.stack = []
        self.topIndex = 0

    def push(self, key):
        self.stack.append(key)
        self.topIndex += 1

    def pop(self):
        if len(self.stack) == 0:
            raise IndexError('cannot pop from an empty list')
        temp = self.stack[self.topIndex - 1]
        del self.stack[self.topIndex - 1]
        self.topIndex -= 1
        return temp

    def isEmpty(self):
        return len(self.stack) == 0

    def __repr__(self):
        return str(self.stack)


# Check if parensthesis match
# true if  "(([]))[]()"
# false if "))()[[()"
def isClosed(s):
    stack = Stack()
    pairs = {
        "(":")",
        "[":"]"
    }

    for c in s:
        if c in ['(', '[']:
            stack.push(c)
        else:
            if stack.isEmpty():
                return False
            else:
                popped = stack.pop()
                if c != pairs[popped]:
                    return False
    return stack.isEmpty()

def main():
    # stack = Stack()
    # for i in range(0, 5):
    #     stack.push(i)
    # print(stack)
    # print(stack.pop())
    # print(stack)
    # print(stack.pop())
    # print(stack)

    print("Testing '(([][]))[[]]()'")
    print(isClosed('(([][]))[[]]()'))
    print()
    print("Testing '))))(()()()[][]]]]))]'")
    print(isClosed('))))(()()()[][]]]]))]'))

if __name__ == "__main__":
    main()
