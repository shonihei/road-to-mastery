# My implementation of Singly Linked List

class Node:
    def __init__(self, val, nextNode=None):
        self.key = val
        self.next = nextNode

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def __len__(self):
        return self.size

    def append(self, key):
        if not self.head:
            self.head = Node(key)
        else:
            self.__appendAux(self.head, key)
        self.size += 1

    def __appendAux(self, node, key):
        if not node.next:
            node.next = Node(key)
            return
        else:
            self.__appendAux(node.next, key)

    def __repr__(self):
        if not self.head:
            return "[]"
        else:
            return self.reprAux(self.head, "[")

    def __reprAux(self, node, s):
        if not node.next:
            return s + str(node.key) + "]"
        else:
            s += str(node.key) + ", "
            return self.__reprAux(node.next, s)

    def popFront(self):
        if not self.head:
            raise IndexError("pop from empty list")
        else:
            self.head = self.head.next
            self.size -= 1

    def removeAt(self, index):
        if index not in range(0, self.size):
            raise IndexError('index out of bounds')
        else:
            self.head = self.__removeAux(self.head, index, 0)
            self.size -= 1

    def __removeAux(self, node, target, cur):
        if target == cur:
            return node.next
        else:
            node.next = self.__removeAux(node.next, target, cur + 1)
            return node

    def __getitem__(self, index):
        if index not in range(0, self.size - 1):
            raise IndexError('index out of bounds')
        else:
            return self.__getItemAux(self.head, index, 0)

    def __getItemAux(self, node, target, cur):
        if target == cur:
            return node.key
        else:
            return self.__getItemAux(node.next, target, cur + 1)

def main():
    ll = SinglyLinkedList()
    ll.append(6)
    ll.append(10)
    print(len(ll))
    print(ll)
    ll.popFront()
    ll.popFront()
    print(ll)
    for i in range(1, 11):
        ll.append(i)
    print(ll)
    ll.removeAt(2)
    print(ll)
    print(ll[2])

if __name__ == "__main__":
    main()
