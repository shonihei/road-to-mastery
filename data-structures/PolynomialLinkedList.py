class Node:
    def __init__(self, coefficient, exponent, n=None, p=None):
        self.coefficient = coefficient
        self.exponent = exponent
        self.next_term = n
        self.prev_term = p
        
class PolynomialLinkedList:
    def __init__(self):
        self.head = None
        self.num_of_terms = 0

    def add_term(self, c, e):
        if not self.head:
            self.head = Node(c, e)
        else:
            self.add_term(self.head, c, e)
        
    def add_aux(self, cur_node, c, e, p):
         
    def __repr__(self):
        out = ""
        if not self.head:
            return "0"
        else:
            cur_node = self.head
            while cur_node:
                c = cur_node.coefficient
                e = cur_node.exponent
                if c >= 0:
                    if cur_node != self.head:
                        out += " + "
                else:
                    out += " - "
                if e == 1:
                    out += str(c)
                elif e == 0:
                    out += "1"
                else:
                    out += str(c) + "^" + str(e)
                cur_node = cur_node.next_term
        return out
    
def main():
    p = PolynomialLinkedList()
    p.add_term(3, 2)
    p.add_term(5, 4)
    print(p)

if __name__ == "__main__":
    main()
