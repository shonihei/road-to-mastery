# task: implement three stacks in a single array

class ThreeStacks:
    SIZE = 100

    def __init__(self):
        self.stacks = [None for i in range(self.SIZE)]
        self.i = 0
        self.ni = self.i
        self.j = self.SIZE // 3
        self.nj = self.j
        self.k = (self.SIZE // 3) * 2
        self.nk = self.k
        
    def push(self, v, i):
        if i > 2:
            raise IndexError("there's three stacks and you asked for more than that")
        if i == 0:
            if self.ni == self.j:
                print("darn")
            self.stacks[self.ni] = v
            self.ni += 1
        elif i == 1:
            if self.nj == self.k:
                print("darn")
            self.stacks[self.nj] = v
            self.nj += 1
        else:
            if self.nk > len(self.stacks) - 1:
                print("darn")
            self.stacks[self.nk] = v
            self.nk += 1

    def pop(self, i):
        if i == 0:
            self.ni -= 1
            return self.stacks[self.ni]
        elif i == 1:
            self.nj -= 1
            return self.stacks[self.nj]
        else:
            self.nk -= 1
            return self.stacks[self.nk]

    def peak_all(self):
        return (self.stacks[self.ni - 1], self.stacks[self.nj - 1], self.stacks[self.nk - 1])

a = ThreeStacks()
a.push(4, 0)
a.push(3, 1)
a.push(7, 2)
print(a.peak_all())
