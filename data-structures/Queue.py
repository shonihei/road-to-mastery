class Node:
    def __init__(self, key, nextNode=None):
        self.key = key
        self.next = nextNode

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def enqueue(self, key):
        if not self.head:
            self.head = Node(key)
            self.tail = self.head
        else:
            self.tail.next = Node(key)
            self.tail = self.tail.next
        self.size += 1

    def dequeue(self):
        if not self.head:
            raise IndexError("cannot dequeue from an empty queue")
        else:
            temp = self.head.key
            self.head = self.head.next
            self.size -= 1
            return temp

    def isEmpty(self):
        return self.size == 0

    def __repr__(self):
        out = "["
        if not self.head:
            return "[]"

        cur = self.head
        while cur.next:
            out += str(cur.key) + ", "
            cur = cur.next
        out += str(cur.key) + "]"
        return out

def main():
    q = Queue()
    q.enqueue(7)
    q.enqueue(10)
    q.enqueue(2)
    q.enqueue(5)
    print(q)
    print("1st dequeue: " + str(q.dequeue()))
    print("2nd dequeue: " + str(q.dequeue()))
    print("3rd dequeue: " + str(q.dequeue()))
    print(q)

if __name__ == "__main__":
    main()
