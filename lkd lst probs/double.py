class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None


class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        if self.head is None:
            return "Linked list is empty"
        else:
            node = self.head
            list_ = []
            while node:
                list_.append(node.data)
                node = node.next
            return list_

    def insert_at_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node

    def insert_at_tail(self, data):
        new_node = Node(data)
        node = self.head
        while node.next:
            node = node.next
        node.next = new_node
        new_node.prev = node

    def insert_at_index(self, index, data):
        new_node = Node(data)
        node = self.head
        if index == 0:
            self.insert_at_head(data)
        else:
            for i in range(index - 1):
                node = node.next
            if node.next is not None:
                node.next.prev = new_node
                new_node.next = node.next
            node.next = new_node
            new_node.prev = node

    def delete_at_head(self):
        node = self.head
        self.head = node.next
        node.next = None
        self.head.prev = None

    def delete_at_tail(self):
        node = self.head.next
        before = self.head
        while node.next is not None:
            node = node.next
            before = before.next
        before.next = None
        node.prev = None

    def delete_at_index(self, index):
        node = self.head.next
        before = self.head
        for i in range(index - 1):
            node = node.next
            before = before.next
        if node.next is not None:
            before.next = node.next
            node.next.prev = before
        else:
            before.next = None
        node.next = None
        node.prev = None


if __name__ == '__main__':
    L = DoubleLinkedList()
    L.insert_at_head(20)
    L.insert_at_head(10)
    L.insert_at_tail(40)
    L.insert_at_tail(50)
    L.insert_at_index(2, 30)
    L.insert_at_index(5, 60)
    L.insert_at_index(0, 0)
    print(L.display())
