import this


class Node:
    def __init__(self, real: float, imaginary: float):
       self.real: float = real
       self.imaginary: float = imaginary
       self.next: Node = None

    def __repr__(self) -> str:
        return f"ComplexNumber(real: float = {self.real}, imaginary: float = {self.imaginary})"

    def __str__(self) -> str:
        return f"{self.real} + {self.imaginary}*i"

    def __eq__(self, other):
        return self.real == other.real and self.imaginary == other.imaginary
    

class StackLinkedList:
    
    def __init__(self):
        self.top: Node = None

    def __repr__(self) -> str:
        result = "StackLinkedList contains: "
        curr = self.top
        index = 0
        while curr is not None:
            result += index + ". " + curr.__repr__() + "\n"
            curr = curr.next
            index += 1
        return result

    def __str__(self) -> str:
        result = ""
        curr = self.top
        if curr is None:
            return "Stack is empty!"
        index = 0
        while curr is not None:
            result += str(index + 1) + ". " + curr.__str__() + "\n"
            curr = curr.next
            index += 1
        return result

    def add_node(self, node: Node):
        node.next = self.top
        self.top = node

    def remove_node(self):
        self.top = self.top.next
    
    def delete_all(self):
        while self.top is not None:
            self.top = self.top.next


    def add(self) -> Node:
        return Node(self.top.real + self.top.next.real, self.top.imaginary + self.top.next.imaginary)

    def find(self, real: float, imaginary: float):
        node = Node(real, imaginary)
        curr = self.top
        index = 0
        while curr is not None:
            if curr == node:
                return "Found node at index " + str(index + 1) + ": " + curr.__str__()
            curr = curr.next
            index += 1
        return "Node not found!"

    def size(self) -> int:
        size = 0
        curr = self.top
        while curr is not None:
            size += 1
            curr = curr.next
        return size

    def print_top(self):
        print(self.top)
    