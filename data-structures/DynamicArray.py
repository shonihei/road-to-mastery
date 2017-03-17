class DynamicArray:
    def __init__(self):
        self.arr = []
        self.nextIndex = 0
        self.size = 0
        self.capacity = 2

    def __str__(self):
        return str(self.arr)

    def full(self):
        return self.capacity == self.size

    def append(self, item):
        if self.full():
            self.resize()
            self.arr += [item]
            self.nextIndex += 1
            self.size += 1
        else:
            self.arr += [item]
            self.nextIndex += 1
            self.size += 1

    def resize(self):
        temp = []
        self.capacity *= 2
        for i in range(0, self.size):
            temp += [self.arr[i]]
        self.arr = temp

def main():
    DA = DynamicArray()
    for i in range(1, 11):
        DA.append(i)
    print(DA)
    print("Size: {}".format(DA.size))
    print("Capacity: {}".format(DA.capacity))

if __name__ == "__main__":
    main()
