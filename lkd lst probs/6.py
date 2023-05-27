# Check if a Linked List is Palindrome: Determine whether a given linked list is a palindrome or not.
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            new_node.next = self.head
            self.head = new_node
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = new_node

    def display(self):
        node = self.head
        lst = []
        while node:
            lst.append(node.data)
            node = node.next
        return lst

    def palindrome(self):
        fast = self.head
        slow = self.head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp

        left = self.head
        right = prev
        while right:
            if left.data != right.data:
                return False
            left = left.next
            right = right.next
        return True


if __name__ == '__main__':
    l = LinkedList()
    for i in [1, 2, 3, 2, 1]:
        l.insert(i)
    print(l.display())
    print(l.palindrome())
