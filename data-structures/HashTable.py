class Node:
    def __init__(self, key, nextNode=None):
        self.key = key
        self.next = nextNode

class HashTable:
    def __init__(self, m):
        self.heads = [None for i in range(m)]
        self.m = m

    def hash(self, key):
        return key % self.m

    def add(self, key):
        h = self.hash(key)
        if not self.heads[h]:
            self.heads[h] = Node(key)
        else:
            newHead = Node(key)
            newHead.next = self.heads[h]
            self.heads[h] = newHead

    def __repr__(self):
        out = ""
        for i in range(len(self.heads)):
            out += str(i) + ": "
            node = self.heads[i]
            if not node:
                out += "\n"
                continue
            while node.next:
                out += str(node.key) + " -> "
                node = node.next
            out += str(node.key) + " -> .\n"
        return out

def main():
    ht = HashTable(10)
    ht.add(12)
    ht.add(15)
    ht.add(3)
    print(ht)
    for i in range(0, 23):
        ht.add(i)
    print(ht)

if __name__ == "__main__":
    main()
