from collections import deque


def balanced_parentheses(exp):
    stack = []
    opening_brackets = ['(', '[', '{']
    closing_brackets = [')', ']', '}']
    for char in exp:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if not stack:
                return False
            top = stack.pop()
            if opening_brackets.index(top) != closing_brackets.index(char):
                return False
    return len(stack) == 0


def reverse_string(string):
    stack = []
    for char in string:
        stack.append(char)
    reversed_string = ""
    while stack:
        reversed_string += stack.pop()
    return reversed_string


def decimal_to_binary(decimal):
    stack = []
    while decimal > 0:
        stack.append(decimal % 2)
        decimal = decimal // 2
    binary = ""
    while stack:
        binary += str(stack.pop())
    return binary


def print_binary_numbers(n):
    queue = deque()
    queue.append("1")
    while n > 0:
        front = queue.popleft()
        print(front)
        queue.append(front + "0")
        queue.append(front + "1")
        n -= 1


# queue using two stacks
class Queue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def is_empty(self):
        return len(self.stack1) == 0 and len(self.stack2) == 0

    def enqueue(self, item):
        self.stack1.append(item)

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        if len(self.stack2) == 0:
            while len(self.stack1) > 0:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()


if __name__ == '__main__':
    # print(decimal_to_binary(42))
    # print(balanced_parentheses("({})"))
    # print(reverse_string("ABCDEF!"))
    # print_binary_numbers(5)
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print(queue.dequeue())
    print(queue.dequeue())
    queue.enqueue(4)
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
