class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def add_data(self, data):
        new_node = Node(data)
        node = self.head
        new_node.next = self.head

        if self.head is not None:
            while node.next != self.head:
                node = node.next
            node.next = new_node
        else:
            new_node.next = new_node
        self.head = new_node

    def display(self):
        node = self.head
        if self.head is not None:
            list_ = []
            while True:
                list_.append(node.data)
                node = node.next
                if node == self.head:
                    break
            return list_


if __name__ == '__main__':
    C = CircularLinkedList()
    C.add_data(10)
    C.add_data(20)
    C.add_data(30)
    print(C.display())
